// adblocker.js
document.addEventListener("DOMContentLoaded", function () {
    // Check if an ad blocker is active
    var adBlockerActive = false;

    var testAd = document.createElement("div");
    testAd.innerHTML = "&nbsp;";
    testAd.className = "ad";

    document.body.appendChild(testAd);

    setTimeout(function () {
        if (testAd.offsetHeight === 0) {
            adBlockerActive = true;
        }
        document.body.removeChild(testAd);

        // If an ad blocker is active, prevent the page from loading
        if (adBlockerActive) {
            document.body.innerHTML = "";
            var messageDiv = document.createElement("div");
            messageDiv.innerHTML =
                '<p>Alaye! This is Timson, abeg remove ads blocker you enabled to visit this site. Thanks.</p>';
            document.body.appendChild(messageDiv);
        }
    }, 100);
});
