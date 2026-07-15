from fastapi import FastAPI


#FastAPI App
app = FastAPI()


# First API Endpoint.
@app.get('/')
def root_check():
    return {'Message':'BankAPI is working!'}