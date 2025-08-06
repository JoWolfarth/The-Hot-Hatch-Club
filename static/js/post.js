const editButtons = document.getElementsByClassName("btn-edit");
const postText = document.getElementById("id_body");
const postForm = document.getElementById("postForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated post's ID upon click.
* - Fetches the content of the corresponding post.
* - Populates the `postText` input/textarea with the post's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_post/{postId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    let postContent = document.getElementById(`post${postId}`).innerText;
    postText.value = postContent;
    submitButton.innerText = "Update";
    postForm.setAttribute("action", `edit_post/${postId}`);
    postForm.style.display = "block";
    });
}