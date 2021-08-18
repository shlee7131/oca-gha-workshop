import sys
import os

getEnvMember1 = os.environ.get("INPUT_MEMBER1")
getEnvMember2 = os.environ.get("INPUT_MEMBER2")

print("Hello " + getEnvMember1)
print("Hello " + getEnvMember2)