# pokelog
(formerly pokediary)
A simple web diary run from a Docker linux container.
Currently in development.

To build:
```
git clone https://github.com/electrachong/pokelog.git
cd Dockerfiles
docker build -t electrachong/pokediary:dev .
```

Run with `docker run -i -t -p 5000:5000 electrachong/pokediary:dev`.

Run `python app.py` and open `0.0.0.0:5000` in browser to see code in instance.
