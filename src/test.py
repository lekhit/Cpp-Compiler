lt=[]
print("""<html lang="en" class="sr">""")
lt.append("""<html lang="en" class="sr">""")
print("""</html>""")
lt.append("""</html>""")
print("""  <head>""")
lt.append("""  <head>""")
print("""  </head>""")
lt.append("""  </head>""")
print("""    <meta charset="utf-8">""")
lt.append("""    <meta charset="utf-8">""")
print("""    </meta>""")
lt.append("""    </meta>""")
print("""    <meta http-equiv="X-UA-Compatible" content="IE=edge">""")
lt.append("""    <meta http-equiv="X-UA-Compatible" content="IE=edge">""")
print("""    </meta>""")
lt.append("""    </meta>""")
print("""    <meta name="viewport" content="width=device-width, initial-scale=1">""")
lt.append("""    <meta name="viewport" content="width=device-width, initial-scale=1">""")
print("""    </meta>""")
lt.append("""    </meta>""")
print("""    <link rel="shortcut icon" type="image/png" href="assets/favicon.png">""")
lt.append("""    <link rel="shortcut icon" type="image/png" href="assets/favicon.png">""")
print("""    </link>""")
lt.append("""    </link>""")
print("""""")
lt.append("""""")
print("""    <title>""")
lt.append("""    <title>""")
print("""    </title>""")
lt.append("""    </title>""")
print("""      Lekhit Borole | Developer""")
lt.append("""      Lekhit Borole | Developer""")
print("""""")
lt.append("""""")
print("""    <meta name="keywords" content="python, lekhit, skill">""")
lt.append("""    <meta name="keywords" content="python, lekhit, skill">""")
print("""    </meta>""")
lt.append("""    </meta>""")
print("""""")
lt.append("""""")
print("""    <meta name="description" content="Lekhit Borole | Developer">""")
lt.append("""    <meta name="description" content="Lekhit Borole | Developer">""")
print("""    </meta>""")
lt.append("""    </meta>""")
print("""""")
lt.append("""""")
print("""    <link rel="stylesheet" href="https>//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">""")
lt.append("""    <link rel="stylesheet" href="https>//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">""")
print("""    </link>""")
lt.append("""    </link>""")
print("""    <link rel="stylesheet" href="styles.scss">""")
lt.append("""    <link rel="stylesheet" href="styles.scss">""")
print("""    </link>""")
lt.append("""    </link>""")
print("""    <script defer src="https>//unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js">""")
lt.append("""    <script defer src="https>//unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js">""")
print("""    </script>""")
lt.append("""    </script>""")
print("""""")
lt.append("""""")
print("""""")
lt.append("""""")
print("""    <script async defer src="https>//buttons.github.io/buttons.js">""")
lt.append("""    <script async defer src="https>//buttons.github.io/buttons.js">""")
print("""    </script>""")
lt.append("""    </script>""")
print("""""")
lt.append("""""")
print("""""")
lt.append("""""")
print("""  <body>""")
lt.append("""  <body>""")
print("""  </body>""")
lt.append("""  </body>""")
print("""    <div id="top">""")
lt.append("""    <div id="top">""")
print("""    </div>""")
lt.append("""    </div>""")
print("""""")
lt.append("""""")
print("""    <section id="hero" class="jumbotron">""")
lt.append("""    <section id="hero" class="jumbotron">""")
print("""    </section>""")
lt.append("""    </section>""")
print("""      <div class="container">""")
lt.append("""      <div class="container">""")
print("""      </div>""")
lt.append("""      </div>""")
print("""        <h1 class="hero-title load-hidden">""")
lt.append("""        <h1 class="hero-title load-hidden">""")
print("""        </h1>""")
lt.append("""        </h1>""")
print("""          Hi, my name is <span class="text-color-main">Lekhit Borole</span>""")
lt.append("""          Hi, my name is <span class="text-color-main">Lekhit Borole</span>""")
print("""          <br />""")
lt.append("""          <br />""")
print("""          I'm the Unknown Developer.""")
lt.append("""          I'm the Unknown Developer.""")
print("""        <p class="hero-cta load-hidden">""")
lt.append("""        <p class="hero-cta load-hidden">""")
print("""        </p>""")
lt.append("""        </p>""")
print("""          <a rel="noreferrer" class="cta-btn cta-btn--hero" href="#about">""")
lt.append("""          <a rel="noreferrer" class="cta-btn cta-btn--hero" href="#about">""")
print("""          </a>""")
lt.append("""          </a>""")
print("""            Know more""")
lt.append("""            Know more""")
print("""    <script defer type="module" src="index.js">""")
lt.append("""    <script defer type="module" src="index.js">""")
print("""    </script>""")
lt.append("""    </script>""")

htmlfile=open("htmlfinal.html","w")
for line in lt:    htmlfile.write(line)
htmlfile.close()