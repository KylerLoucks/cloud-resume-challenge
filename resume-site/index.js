update()

// Make an API call to grab data containing streamer status
async function getStreamData() {
    const res = await fetch("https://0uywkvq4m7.execute-api.us-east-1.amazonaws.com/Prod/get", {
    method: 'GET',
    mode: 'cors',
    });
    const json = await res.json();
    return json;
}

async function updateDynamoDBTable() {
    const res = await fetch("https://0uywkvq4m7.execute-api.us-east-1.amazonaws.com/Prod/post", {
    method: 'POST',
    });
}

async function update() {
    const responseData = await getStreamData();
    const viewCountElement = document.getElementById("views").innerText = "Viewer Count: " + responseData.count;
    await updateDynamoDBTable();
}


