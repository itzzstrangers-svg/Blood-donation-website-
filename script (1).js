<!DOCTYPE html>
<html>
<head>
<title>3D Blood Donation Website</title>

<style>
body{
    margin:0;
    font-family:Arial;
    background:linear-gradient(135deg,#ff0000,#800000);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.container{
    display:flex;
    gap:30px;
    flex-wrap:wrap;
}

.card{
    width:250px;
    height:250px;
    background:white;
    border-radius:20px;
    text-align:center;
    padding:20px;
    box-shadow:0 20px 40px rgba(0,0,0,0.5);
    transform:rotateY(-10deg);
    transition:0.5s;
}

.card:hover{
    transform:rotateY(0deg) translateY(-15px);
}

h1{
    color:white;
    position:absolute;
    top:20px;
}

h2{
    color:red;
}

button{
    background:red;
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:20px;
    cursor:pointer;
}

button:hover{
    background:darkred;
}

</style>

</head>

<body>

<h1>🩸 Blood Donation System</h1>

<div class="container">

<div class="card">
<h2>Donate Blood</h2>
<p>Become a life saver by donating blood.</p>
<button onclick="donate()">Donate Now</button>
</div>


<div class="card">
<h2>Request Blood</h2>
<p>Find blood during emergency.</p>
<button onclick="requestBlood()">Request</button>
</div>


<div class="card">
<h2>Blood Groups</h2>
<p>Check available blood groups.</p>
<button onclick="showGroups()">View</button>
</div>

</div>


<script>

function donate(){
    alert("Thank you for registering as a blood donor ❤️");
}

function requestBlood(){
    alert("Blood request form opened.");
}

function showGroups(){
    alert("Available Groups: A+, A-, B+, B-, AB+, AB-, O+, O-");
}

</script>

</body>
</html>