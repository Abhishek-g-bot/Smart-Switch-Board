// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyAekx7jVs-uyVqoH7ZiU_lozoYEBAFvhmA",
    authDomain: "smartswitchboard2022.firebaseapp.com",
    databaseURL: "https://smartswitchboard2022-default-rtdb.firebaseio.com",
    projectId: "smartswitchboard2022",
    storageBucket: "smartswitchboard2022.appspot.com",
    messagingSenderId: "684992482262",
    appId: "1:684992482262:web:e3295940648ec613d27277",
    measurementId: "G-W88GGR41VD"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

$(document).ready(function(){
var database = firebase.database();
var Led1Status;
var Led2Status;
var Led3Status;
var Led4Status;
database.ref().on("value", function(snap){
  Led1Status = snap.val().Led1Status;
  Led2Status = snap.val().Led2Status;
  Led3Status = snap.val().Led3Status;
  Led4Status = snap.val().Led4Status;
  if(Led1Status == "1"){
    document.getElementById("unact").style.display = "none";
    document.getElementById("act").style.display = "block";
  } else {
    document.getElementById("unact").style.display = "block";
    document.getElementById("act").style.display = "none";
  }
  if(Led2Status == "1"){
    document.getElementById("unact1").style.display = "none";
    document.getElementById("act1").style.display = "block";
  } else {
    document.getElementById("unact1").style.display = "block";
    document.getElementById("act1").style.display = "none";
  }
  if(Led3Status == "1"){
    document.getElementById("unact2").style.display = "none";
    document.getElementById("act2").style.display = "block";
  } else {
    document.getElementById("unact2").style.display = "block";
    document.getElementById("act2").style.display = "none";
  }
  if(Led4Status == "1"){
    document.getElementById("unact3").style.display = "none";
    document.getElementById("act3").style.display = "block";
  } else {
    document.getElementById("unact3").style.display = "block";
    document.getElementById("act3").style.display = "none";
  }
});

$(".toggle-btn").click(function(){
  var firebaseRef = firebase.database().ref().child("Led1Status");
  if(Led1Status == "1"){
    firebaseRef.set("0");
    Led1Status = "0";
  } else {
    firebaseRef.set("1");
    Led1Status = "1";
  }
})
$(".toggle-btn1").click(function(){
  var firebaseRef = firebase.database().ref().child("Led2Status");
  if(Led2Status == "1"){
    firebaseRef.set("0");
    Led2Status = "0";
  } else {
    firebaseRef.set("1");
    Led2Status = "1";
  }
})
$(".toggle-btn2").click(function(){
  var firebaseRef = firebase.database().ref().child("Led3Status");
  if(Led3Status == "1"){
    firebaseRef.set("0");
    Led3Status = "0";
  } else {
    firebaseRef.set("1");
    Led3Status = "1";
  }
})
$(".toggle-btn3").click(function(){
  var firebaseRef = firebase.database().ref().child("Led4Status");
  if(Led4Status == "1"){
    firebaseRef.set("0");
    Led4Status = "0";
  } else {
    firebaseRef.set("1");
    Led4Status = "1";
  }
})
document.getElementById('hand-gesture-button').addEventListener('click', function() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/video_feed', true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      // handle the response from the server
      var result = xhr.responseText;
      alert(result);
    }
  };
  xhr.send();
});
});
