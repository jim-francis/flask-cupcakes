const apiURL = "http://127.0.0.1:5000/api"

function getCupcakeHTML(cupcake){
    return `
    <div data-id=${cupcake.id}>
        <li>
        ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button">X</button>
        </li>
        <img class="cupcake-img" src="${cupcake.image}" alt="(no image)">
        </div>
    `;
}

async function showCupcakes(){
    const res = await axios.get(`${apiURL}/cupcakes`)

    for (let cupcake of res.data.cupcakes){
        let newCupcake = getCupcakeHTML(cupcake);
        $("#cupcake-list").append(newCupcake);
        console.log(newCupcake)
    }
}

showCupcakes()