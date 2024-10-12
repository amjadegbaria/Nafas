let startTime = Date.now();
let countDirection = 1; // 1 for incrementing, -1 for decrementing
let currentCount = 1; // Start from 1
const maxCount = 6;   // Maximum value for the counter
const minCount = 1;   // Minimum value for the counter
const intervalDuration = 1000; // 1 second in milliseconds
let phaseText = "شهيق";


function updateCounter() {
    const now = Date.now();
    const elapsedTime = Math.floor((now - startTime) / intervalDuration); // Time in seconds

    if (elapsedTime >= 1) {
        // Update the counter value
        currentCount += countDirection;

        // Check if we need to reverse the counting direction
        if (currentCount >= maxCount) {
		setTimeout(6000);
		document.getElementById('circle').className = "circle-exhale";
		phaseText ="زفير"
            countDirection = -1; // Switch to decrementing
        } else if (currentCount <= minCount) {
		document.getElementById('circle').className = "circle";
		phaseText ="شهيق"
            countDirection = 1;  // Switch to incrementing
        }

        // Reset start time to align with the second-based increments
        startTime = Date.now();
    }

        document.getElementById('phaseText').textContent = phaseText;

}

setInterval(updateCounter, 100); // Update every 100ms for smoother transition
