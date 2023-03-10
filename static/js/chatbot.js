function show(x) {
    let answer = document.getElementById("ans");
    if (x == 0) {
        /* answer.innerHTML = " This is diet plan"; */
        window.location.href = "/diet";
    }
    else if (x == 1) {
        window.location.href = "/physio";
    }
    else if (x == 2) {
        window.location.href = "/payment";
    }
}

var count = 0;

function display() {
    count++;
    let answer = document.getElementById("chatbot");
    let btn = document.getElementById("chatbot_btn");
    let greet = document.getElementById("chatbot_greeting");

    if (count % 2 == 1) {
        answer.style.visibility = "visible";
        answer.style.animation = "animate 1s";
        btn.innerHTML = "<br>Cancel";
    }
    else {
        answer.style.visibility = "hidden";
        btn.innerHTML = "Check out here!";
    }
}

function suggestHospital() {
    suggest = {
        "lung": "Suggested hospital is: " + "<a href='http://www.hcghospitals.in/'>HCG Hospital<a>" + "<br>Suggested doctor: Dr. Ram"
        ,"blood":"Suggested hospital is: " + "<a href='https://apollocbcc.com/'>Apollo Comprehensive Blood & Cancer Centre<a>" + "<br>Suggested doctor: Dr. Mukesh"
        ,"breast":"Suggested hospital is: "  + "<a href='https://www.breastcentreindia.com/'>Dr. Shefali Desai, Breast Care Clinic, Samved Hospital, </a><br><a href='http://www.drtarangpatel.in/'>Dr. Tarang Patel, Breast & Thyroid Cancer Specialist Surgeon</a>" + "<br>Suggested doctor: Dr. Nayan"
        ,"prostate":"Suggested hospital is: "  + "<a href='http://www.drkevalpatel.com/'>Ayushyam Hospital<a>" + "<br>Suggested doctor: Dr. Keshav"
        ,"bladder":"Suggested hospital is: "  + "<a href='http://www.zanishcancerhospital.com/'>Zanish cancer Hospital<a>" + "<br>Suggested doctor: Dr. Dharmesh"
        ,"tongue":"Suggested hospital is: "  + "<a href='http://www.drbhargavmaharaja.in/'>Dr. Bhargav Maharaja-Tongue Cancer Surgeon<a>" + "<br>Suggested doctor: Dr. Rakesh"
        ,"head and neck":"Suggested hospital is: "  + "<a href='https://www.headandneckcancercare.in/'>Head And Neck Cancer Care<a>" + "<br>Suggested doctor: Dr. Suresh"
        ,"":"Please select cancer type..."
    }
    var u = document.getElementById("cancer_type").value;
    
    userip = u.toLowerCase();
    var answer = document.getElementById("suggest");

    answer.style.cssText = "color: black;font-size: 2em;";
    if (userip in suggest) {
        answer.innerHTML = suggest[userip];
    }
    else {
        answer.innerHTML = "Can not find hospital.";
    }
}

function onload() {
    swal('This is CPMS website for Cancer patients.... This alert is for testing purpose.');
}

