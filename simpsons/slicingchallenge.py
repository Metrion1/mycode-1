#!/usr/bin/env python3

def main():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


    e= challenge[2][1]
    g= challenge[2][0]
    n= challenge[3]

    print(f"My {e}! The {g} do {n}!")
    

    a= trial[2]["goggles"]
    s= trial[2]["eyes"]
    d= trial[-1]

    print(f"My {a}! The {s} do {d}!")
main()
