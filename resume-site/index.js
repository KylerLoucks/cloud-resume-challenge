update()

// Make an API call to grab data containing viewer count
async function getStreamData() {
    const res = await fetch("https://api.kylerloucks.click/get", {
    method: 'GET',
    mode: 'cors',
    });
    const json = await res.json();
    return json;
}

async function updateDynamoDBTable() {
    const res = await fetch("https://api.kylerloucks.click/post", {
    method: 'POST',
    });
}

async function update() {
    const responseData = await getStreamData();
    const viewCountElement = document.getElementById("views").innerText = "Viewer Count: " + responseData.count;
    await updateDynamoDBTable();
}


