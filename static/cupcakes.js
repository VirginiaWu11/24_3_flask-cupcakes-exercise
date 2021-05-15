$("#new-cupcake").on("submit", handleSubmit);

function generateCupcakeHTML(cupcake) {
  return `
    <div data-cupcake-id=${cupcake.id}>
      <li> ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
      <button class="delete-button">Delete</button>
      </li>
      <img src="${cupecake.image}"
      </div>
      `;
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
}
