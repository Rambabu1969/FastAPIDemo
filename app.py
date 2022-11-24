
# 1. Library imports
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
from house import house

# 2. Create the app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. load the model
model = pickle.load(open("rf.pkl", "rb"))

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get("/predictPrice")
def getPredictPrice(Area: int, BedRooms: int, BathRooms: int):
    rgModel = pickle.load(open("reg.pkl", "rb"))
    
    prediction = rgModel.predict([[Area,BedRooms,BathRooms]])
    
    return {
        'Price': prediction[0]
    }

@app.post("/predict")
def predictHousePrice(data: house):
    rgModel = pickle.load(open("reg.pkl", "rb"))

    data = data.dict()
    prediction = rgModel.predict([[data["Area"],data["BedRooms"],data["BathRooms"]]])
    
    return {
        'Price': prediction[0]
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    
#uvicorn app:app --reload
