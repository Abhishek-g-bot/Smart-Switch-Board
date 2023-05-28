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
firebase.initializeApp(firebaseConfig);
$(document).ready(function(){
var database = firebase.database();
var Relay1Status;
var Relay2Status;
var Relay3Status;
var Relay4Status;
var Relay5Status;
var Relay6Status;
var Relay7Status;
var Relay8Status;
database.ref().on("value", function(snap){
Relay1Status = snap.val().Relay1Status;
Relay2Status = snap.val().Relay2Status;
Relay3Status = snap.val().Relay3Status;
Relay4Status = snap.val().Relay4Status;
Relay5Status = snap.val().Relay5Status;
Relay6Status = snap.val().Relay6Status;
Relay7Status = snap.val().Relay7Status;
Relay8Status = snap.val().Relay8Status;
if(Relay1Status == "1"){
  document.getElementById("unact").style.display = "none";
  document.getElementById("act").style.display = "block";
} else {
  document.getElementById("unact").style.display = "block";
  document.getElementById("act").style.display = "none";
}
if(Relay2Status == "1"){
  document.getElementById("unact1").style.display = "none";
  document.getElementById("act1").style.display = "block";
} else {
  document.getElementById("unact1").style.display = "block";
  document.getElementById("act1").style.display = "none";
}
if(Relay3Status == "1"){
  document.getElementById("unact2").style.display = "none";
  document.getElementById("act2").style.display = "block";
} else {
  document.getElementById("unact2").style.display = "block";
  document.getElementById("act2").style.display = "none";
}
if(Relay4Status == "1"){
  document.getElementById("unact3").style.display = "none";
  document.getElementById("act3").style.display = "block";
} else {
  document.getElementById("unact3").style.display = "block";
  document.getElementById("act3").style.display = "none";
}
if(Relay5Status == "1"){
  document.getElementById("unact4").style.display = "none";
  document.getElementById("act4").style.display = "block";
} else {
  document.getElementById("unact4").style.display = "block";
  document.getElementById("act4").style.display = "none";
}
if(Relay6Status == "1"){
  document.getElementById("unact5").style.display = "none";
  document.getElementById("act5").style.display = "block";
} else {
  document.getElementById("unact5").style.display = "block";
  document.getElementById("act5").style.display = "none";
}
if(Relay7Status == "1"){
  document.getElementById("unact6").style.display = "none";
  document.getElementById("act6").style.display = "block";
} else {
  document.getElementById("unact6").style.display = "block";
  document.getElementById("act6").style.display = "none";
}
if(Relay8Status == "1"){
  document.getElementById("unact7").style.display = "none";
  document.getElementById("act7").style.display = "block";
} else {
  document.getElementById("unact7").style.display = "block";
  document.getElementById("act7").style.display = "none";
}
});

$(".toggle-btn").click(function(){
var firebaseRef = firebase.database().ref().child("Relay1Status");
if(Relay1Status == "1"){
  firebaseRef.set("0");
  Relay1Status = "0";
} else {
  firebaseRef.set("1");
  Relay1Status = "1";
}
})
$(".toggle-btn1").click(function(){
var firebaseRef = firebase.database().ref().child("Relay2Status");
if(Relay2Status == "1"){
  firebaseRef.set("0");
  Relay2Status = "0";
} else {
  firebaseRef.set("1");
  Relay2Status = "1";
}
})
$(".toggle-btn2").click(function(){
var firebaseRef = firebase.database().ref().child("Relay3Status");
if(Relay3Status == "1"){
  firebaseRef.set("0");
  Relay3Status = "0";
} else {
  firebaseRef.set("1");
  Relay3Status = "1";
}
})
$(".toggle-btn3").click(function(){
var firebaseRef = firebase.database().ref().child("Relay4Status");
if(Relay4Status == "1"){
  firebaseRef.set("0");
  Relay4Status = "0";
} else {
  firebaseRef.set("1");
  Relay4Status = "1";
}
})
$(".toggle-btn4").click(function(){
  var firebaseRef = firebase.database().ref().child("Relay5Status");
  if(Relay5Status == "1"){
    firebaseRef.set("0");
    Relay5Status = "0";
  } else {
    firebaseRef.set("1");
    Relay5Status = "1";
  }
  })
$(".toggle-btn5").click(function(){
var firebaseRef = firebase.database().ref().child("Relay6Status");
if(Relay6Status == "1"){
  firebaseRef.set("0");
  Relay6Status = "0";
} else {
  firebaseRef.set("1");
  Relay6Status = "1";
}
})
$(".toggle-btn6").click(function(){
  var firebaseRef = firebase.database().ref().child("Relay7Status");
  if(Relay7Status == "1"){
    firebaseRef.set("0");
    Relay7Status = "0";
  } else {
    firebaseRef.set("1");
    Relay7Status = "1";
  }
})
$(".toggle-btn7").click(function(){
  var firebaseRef = firebase.database().ref().child("Relay8Status");
  if(Relay8Status == "1"){
    firebaseRef.set("0");
    Relay8Status = "0";
  } else {
    firebaseRef.set("1");
    Relay8Status = "1";
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
