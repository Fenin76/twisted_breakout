import pickle

with open("score.bin", "rb") as f:
    hs = pickle.load(f)

with open("score.bin", "wb") as f:   
    pickle.dump(0, f)

print(f" HIGH SCORE changed from {hs} to 0")