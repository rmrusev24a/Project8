import streamlit as st

st.title("Gallery of favourite movies")

if "movies" not in st.session_state:
  st.session_state.movies = []

st.header("Add new movie")
name = st.text_input("Name of movie")
description = st.text_area("Description")
image_url = st.text_input("URL of image")

if st.button("Add"):
  if name and discription and image_url:
    st.session_state.movies.append({
      "name": name,
      "description": description,
      "image": image_url
    })
    st.success(f"{name} is added!")
  else:
    st.warning("Fill every field!")

if st.session_state.animals:
  st.header("Remove movie")

  name = []
  for a in st.session_state.movies:
    names.append(a["name"])

    remove_name = st.selectbox("Choose movie to remove", names)
    
if st.button("Remove"):
  for a in st.session_state.movies:
    if a["name"] == remove_name:
      st.session_state.movies.remove(a)
      break
  st.success(f"{remove_name} is removed!")

st.header("Gallery")
if st.session_state.movies:
  cols = st.columns(3)
  for idx, animal in enumerate(st.session_state.movies):
    with cols[idx % 3]:
      st.subheader(movie["name"])
      st.image(movie["image"], use_column_width=True)
      st.write(movie["description"])
else:
  st.info("Gallery is empty. Add movies!")
  
