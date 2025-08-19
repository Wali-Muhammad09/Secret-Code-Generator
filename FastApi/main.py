import streamlit as st
import plotly.express as px
from fastapi import FastAPI as fa
import uvicorn

my_app = fa()
l = ["Cool stuff"]
my_app.get('/')

my_app.post("/idk")
def create_s(i: str):
    l.append(i)
    return l