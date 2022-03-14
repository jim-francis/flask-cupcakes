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

$("#add-cupcake-form").on("submit", async function(e){
    e.preventDefault();
    let flavor = $("#form-flavor").val();
    let size = $("#form-size").val();
    let rating = $("#form-rating").val();
    let image = $("#form-image").val();

    const postedCupcake = await axios.post(`${apiURL}/cupcakes`, {
        flavor,
        size,
        rating,
        image
    })

    let newCupcake = showCupcakes(postedCupcake.data.cupcake)
    $("#cupcake-list").append(newCupcake)
    $("#add-cupcake-form").trigger("reset");
})

$("#cupcake-list").on("click", ".delete-button", async function(e){
    e.preventDefault()
    let cupcake = $(e.target).closest("div");
    let cupcakeID = cupcake.attr("data-id")

    await axios.delete(`${apiURL}/cupcakes/${cupcakeID}`)
    cupcake.remove();
})

showCupcakes()