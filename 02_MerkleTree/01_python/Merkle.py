import hashlib

# Function to compute the hash of a block of data
# ပေးလိုက်တဲ data ပေါ်မူတည်ပြီး Sha256 hash ထုတ်ပေးမယ်။
def compute_hash(data):
    return hashlib.sha256(data).hexdigest()

# Class for Merkle Tree
class MerkleTree:
    def __init__(self, data):
        self.leaves = [compute_hash(d.encode()) for d in data]
        self.build_tree()

    # build_tree function က ပေးလိုက်တဲ့ hash တွေကို pari အလိုက် recursively combines လုပ်ပြီး 
    # binary structure tree node တွေဆောက်မယ်
    def build_tree(self):
        if len(self.leaves) == 1:
            return
        next_level = []
        for i in range(0, len(self.leaves), 2):
            combined = self.leaves[i] + self.leaves[i + 1]
            next_level.append(compute_hash(combined.encode()))
        self.leaves = next_level
        self.build_tree()

    # ဒီ Function ကတော့ Merkle root hash ကိုယူဖို့ Getter မျိုး
    def get_root(self):
        return self.leaves[0]

# Example usage
data = ["Transaction1", "Transaction2", "Transaction3", "Transaction4"]
merkle_tree = MerkleTree(data)

print("Merkle Root:", merkle_tree.get_root())
