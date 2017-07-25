<?php
session_start();
?>
<!DOCTYPE html>
<html>
<head>
<title>Home</title>
<link href="css/bootstrap.css" type="text/css" rel="stylesheet" media="all">
<link href="css/style.css" type="text/css" rel="stylesheet" media="all">
<!-- Custom Theme files -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Crops Responsive web template, Bootstrap Web Templates, Flat Web Templates, Andriod Compatible web template, 
	Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyErricsson, Motorola web design" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- //Custom Theme files -->
<!-- js -->
<script src="js/jquery-1.11.1.min.js"></script> 
<!-- //js -->	
<!-- start-smoth-scrolling-->
<script type="text/javascript" src="js/move-top.js"></script>
<script type="text/javascript" src="js/easing.js"></script>	
<script type="text/javascript">
		jQuery(document).ready(function($) {
			$(".scroll").click(function(event){		
				event.preventDefault();
				$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
			});
		});
</script>
<!--//end-smoth-scrolling-->
</head>
<body>
	<!--header-->
	<div class="logo">
		<div class="container">
			<div class="logo-info">
				<a href="index.php">
					<h1>Diet OPtimization</h1>	
					<span class="glyphicon glyphicon-grain" aria-hidden="true"></span>
				</a>
			</div>
		</div>	
	</div>
	<!--//header-->		
	<!--navigation-->
	<div class="top-nav">
		<nav class="navbar navbar-default">
			<div class="container">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">Menu						
				</button>
			</div>
			<!-- Collect the nav links, forms, and other content for toggling -->
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				<ul class="nav navbar-nav">
					<li class="hvr-bounce-to-bottom"><a href="index.php">Home</a></li>
					<li class="hvr-bounce-to-bottom"><a href="deit.php">My Diet</a></li>
					<li><a href="#" class="dropdown-toggle hvr-bounce-to-bottom" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Food Catalog<span class="caret"></span></a>
						<ul class="dropdown-menu">
							<li><a class="hvr-bounce-to-bottom" href="carbohyrate.php">Carbohydrate</a></li>
							<li><a class="hvr-bounce-to-bottom" href="fruit.php">Fruit</a></li>
							<li><a class="hvr-bounce-to-bottom" href="protein.php">Protein</a></li> 
                            <li><a class="hvr-bounce-to-bottom" href="vegetable.php">Vegatables</a></li>           
						</ul>
					</li>	
					<li class="hvr-bounce-to-bottom" active><a href="account.php">My Account</a></li>
					<li class="hvr-bounce-to-bottom"><a href="search.php">Search</a></li>
				</ul>		
				<div class="clearfix"> </div>
			</div>	
		</nav>		
	</div>	
    <div class="login_form">
          
          <?PHP
                
				if( isset($_SESSION["name"]) )
				{
					print("
					
					Hi,".$_SESSION["name"].".
					
					
					
					"
					 
					);
					print("<a href='logoff.php' class='username'>Log off</a>");
					}
				if( !isset($_SESSION["name"]) )
			    {
				print("
				
                <div class='form_subtitle'>Create your acount</div>
				<form name='register' action='registerprocess.php' method='post' onsubmit='return checkForm(this);'>          
                    <div class='login_row'>
                    <label class='login' ><strong>Name:</strong></label>
                    <input type='text' class='login_input' name='username' id='username1' />
                    <label class='check' id='username' ><strong></strong></label>
                    </div>  


                    <div class='login_row'>
                    <label class='login' ><strong>Password:</strong></label>
                    <input type='password' class='login_input' name='password' id='userpassword1' />
                    <label class='check' id='password' ><strong></strong></label>
                    </div> 
					<div class='login_row'>
                    <label class='login' ><strong>Email:</strong></label>
                    <input type='text' class='login_input' name='Email' id='Email1' />
                    <label class='check' id='Email' ><strong></strong></label>
                    </div> 
					                  
                    <div class='login_row'>
                    
				    
					<input type='submit' class='submit_login' value='register' />
                    </div>   
                    
                  </form>     
				  
				  ");
				
				}
                ?>
        </div>
<div class="footer">	
		<div class="container">
			<div class="footer-grids">
				<div class="col-md-3 footer-grid">
					<h3 class="title">Services</h3>
					<ul>
						<li><a href="#">Rerum hic tenetur</a></li>
						<li><a href="#">Molestiae non recusandae</a></li>
						<li><a href="#">Voluptates repudiandae</a></li>
						<li><a href="#">Necessitatibus saepe</a></li>
						<li><a href="#">Debitis aut rerum</a></li>
					</ul>
				</div>
				<div class="col-md-3 footer-grid">
					<h3 class="title">Information</h3>
					 <ul>
						<li><a href="#">Quibusdam et aut</a></li>
						<li><a href="#">Testimonals</a></li>
						<li><a href="#">Archives</a></li>
						<li><a href="#">Our Staff</a></li>
					</ul>
				</div>
				<div class="col-md-3 footer-grid">
					<h3 class="title">More details</h3>
					<ul>
						<li><a href="about.html">About us</a></li>
						<li><a href="#">Privacy Policy</a></li>
						<li><a href="#">Terms &amp; Conditions</a></li>
						<li><a href="contact.html">Site map</a></li>
					</ul>
				</div>
				<div class="col-md-3 footer-grid contact-grid">
						<h3 class="title">Contact us</h3>
						<ul>
							<li><span class="glyphicon glyphicon-map-marker" aria-hidden="true"></span>Newyork Still Road.</li>							
							<li class="adrs">756 gt globel Place</li>
							<li><span class="glyphicon glyphicon-earphone" aria-hidden="true"></span>+000 100 444 1111</li>
							<li><span class="glyphicon glyphicon-envelope" aria-hidden="true"></span><a href="mailto:example@mail.com">mail@example.com</a></li>
						</ul>
				</div>
				<div class="clearfix"> </div>
			</div>
		</div>
	</div>
	<div class="copy">
		<div class="container">
			<div class="copy-left">
				<p>Copyright &copy; 2015.Company name All rights reserved.<a target="_blank" href="http://www.cssmoban.com/">&#x7F51;&#x9875;&#x6A21;&#x677F;</a></p>
			</div>
			<div class="social-icons">
				<ul>
					<li><a href="#" class="fb"></a></li>
					<li><a href="#"></a></li>
					<li><a href="#" class="gg"></a></li>
					<li><a href="#" class="pn"></a></li>					
				</ul>	
			</div>
			<div class="clearfix"> </div>
		</div>
	</div>
	<!--//footer-->
	<!--smooth-scrolling-of-move-up-->
	<script type="text/javascript">
		$(document).ready(function() {
			/*
			var defaults = {
				containerID: 'toTop', // fading element id
				containerHoverID: 'toTopHover', // fading element hover id
				scrollSpeed: 1200,
				easingType: 'linear' 
			};
			*/
			
			$().UItoTop({ easingType: 'easeOutQuart' });
			
		});
	</script>
	<a href="#" id="toTop" style="display: block;"> <span id="toTopHover" style="opacity: 1;"> </span></a>
	<!--//smooth-scrolling-of-move-up-->
	<!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/bootstrap.js"></script>
</body>
</html>