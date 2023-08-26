from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample data - Replace with your actual data and logic
users = {
    "user1": {
        "address": "0x1234567890abcdef",
        "tokens": {
            "token1": {
                "name": "Carbon Credit NFT",
                "metadata_ipfs_hash": "YOUR_METADATA_IPFS_HASH",
            }
        }
    }
}

class TokenTransfer(BaseModel):
    from_user: str
    to_user: str
    token_id: str

# Routes
@app.get('/get_tokens/{user}')
def get_tokens(user: str):
    user = users.get(user)
    if user:
        return user.get('tokens', {})
    return {"error": "User not found"}

@app.post('/transfer_token')
def transfer_token(data: TokenTransfer):
    from_user_data = users.get(data.from_user)
    to_user_data = users.get(data.to_user)
    
    if from_user_data and to_user_data:
        token_data = from_user_data['tokens'].pop(data.token_id, None)
        if token_data:
            to_user_data['tokens'][data.token_id] = token_data
            return {"message": "Token transferred successfully"}
    
    return {"error": "Transfer failed"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

