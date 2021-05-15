$("#new-cupcake").on("submit", handleSubmit);

function generateCupcakeHTML(cupcake) {
  return `
    <div data-cupcake-id=${cupcake.id}>
      <li> ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
      <button class="delete-button">Delete</button>
      </li>
      <img src="${cupcake.image}", height="200px"
      </div>
      `;
}
async function showInitialCupcakes() {
  const response = await axios.get(`/api/cupcakes`);
  for (let cupcakeData of response.data.cupcakes) {
    let newCupcake = $(generateCupcakeHTML(cupcakeData));
    $("#cupcakes-list").append(newCupcake);
  }
}

async function handleSubmit(evt) {
  evt.preventDefault();

  let flavor = $("#flavor").val();
  let rating = $("#rating").val();
  let size = $("#size").val();
  let image = $("#image").val();
  console.log(size);
  const newCupcakeResponse = await axios.post("api/cupcakes", {
    flavor,
    rating,
    size,
    image,
  });
  console.log(newCupcakeResponse);

  let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
  $("#cupcakes-list").append(newCupcake);
  $("#new-cupcake").trigger("reset");
}
$(showInitialCupcakes);
