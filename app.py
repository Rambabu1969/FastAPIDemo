# Download and Install Python from https://www.python.org/downloads
# pip install fastapi uvicorn scikit-learn

# 1. Library imports
import uvicorn
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import pickle

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
rgModel = pickle.load(open("reg.pkl", "rb"))

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get("/predictPrice")
def gePredictPrice(Area: int, BedRooms: int, BathRooms: int):
    prediction = rgModel.predict([[Area,BedRooms,BathRooms]])
    return {'Price': prediction[0]}

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')
    
# Run Program: uvicorn app:app --host 0.0.0.0 --port 80
# Browse URL: http://127.0.0.1/predictPrice?Area=1400&BedRooms=3&BathRooms=3

