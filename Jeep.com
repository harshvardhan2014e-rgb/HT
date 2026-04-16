<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WWW.Jeep.com</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="style.css">
</head>

<body data-bs-spy="scroll" data-bs-target="#navbar" data-bs-offset="50" tabindex="0">

    <!-- Home Section with Carousel -->
    <section id="home" class="pt-5 mt-5">
        <div id="portfolioCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="American Design GIF by Namaste Car.gif" class="d-block w-100" alt="Project 1">
                </div>
                <div class="carousel-item">
                    <img src="https://www.usnews.com/object/image/00000194-1f21-de56-a19c-7f3938060000/usnpx-25jeepgrandcherokee4xe-jmv-0029.jpg?update-time=1735689057644&size=responsiveGallery" class="d-block w-100" alt="Project 2">
                </div>
                <div class="carousel-item">
                    <img src="https://cdn.motor1.com/images/mgl/1ZQZAw/s1/2024-jeep-gladiator-rubicon-x.jpg" class="d-block w-100" alt="Project 3">
                </div>
                </button>
            </div>
    </section>

    <!-- Navbar -->
    <nav id="navbar" class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top shadow">
        <div class="container-fluid">
            <a class="navbar-brand fw-bold text-" href="#">Jeep</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navMenu">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">vehicles</a></li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="servicesDropdown" role="button"
                            data-bs-toggle="dropdown">
                            Services
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#web">service1</a></li>
                            <li><a class="dropdown-item" href="#consulting">service2</a></li>
                            <li><a class="dropdown-item" href="#marketing">service3</a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="#team">Team</a></li>
                    <li class="nav-item"><a class="nav-link" href="#review">Review</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    
<!-- About Jeep -->
 <br>
 <br>
<section id="about">
    <h2>About Jeep</h2>
    <p>Jeep is a brand of Stellantis known for rugged SUVs and off-road capability.
        From the iconic Wrangler to the versatile Grand Cherokee, Jeep vehicles are
        built to deliver adventure, freedom, and durability.</p>
</section>
    <!-- Vehicle List -->
     <br>
    <main id="vehicles">
        <h2>Our Vehicles</h2>
        <div class="grid">
            <div class="card">
                <img src="https://www.jeep.com/mediaserver/iris?client=FCAUS&market=U&brand=J&vehicle=2026_JL&paint=PW7&fabric=X9&sa=JLJL74%2C2TW%2C22W%2CPW7%2CX9%2C-X9%2CAJK%2CCWA%2CGCD%2CHT1&resp=png&bkgnd=white&pov=fronthero"  width="700


                " alt="Wrangler">
                <h3>Wrangler</h3>
                <p>MSRP Starting at $36,035</p>
                <br>
            </div>
            <div class="card">
                <img src="https://www.motortrend.com/uploads/2023/01/2023-Jeep-Cherokee-Exterior-6.jpg" width="700
                "
                    alt="Cherokee">
                <h3>Cherokee</h3>
                <p>MSRP Starting at $35,000</p>
                <br>
            </div>
            <div class="card">
                <img src="https://www.usnews.com/object/image/00000194-89b3-dc0d-a5ff-8bb3b84a0000/01-usnpx-2025jeepgrandcherokee-angularfront-jms.jpg?update-time=1737477043916&size=responsiveGallery" width="700"
                    alt="Grand Cherokee">
                <h3>Grand Cherokee</h3>
                <p>MSRP Starting at $37,095</p>
                <br>
            </div>
            <div class="card">
                <img src="https://cdn.motor1.com/images/mgl/LEqMM/s3/2020-jeep-gladiator-launch-edition.jpg"  width="700"    alt="Gladiator">
                <h3>Gladiator</h3>
                <p>MSRP Starting at $40,015</p>
                <br>
            </div>
        </div>
    </main>

  

    <!-- Footer -->
    <footer class="bg-dark text-white text-center p-4 mt-5">
        <p>&copy; 2026 Jeep. All rights reserved.</p>
        <div>
            <a href="#" class="text-white me-3"><i class="bi bi-facebook"></i></a>
            <a href="#" class="text-white me-3"><i class="bi bi-twitter"></i></a>
            <a href="#" class="text-white"><i class="bi bi-linkedin"></i></a>
        </div>
    </footer>
</body>

</html>