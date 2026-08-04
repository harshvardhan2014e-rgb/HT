// Select HTML elements
const noteInput = document.getElementById("noteInput");
const addBtn = document.getElementById("addBtn");
const notesContainer = document.getElementById("notesContainer");

// Add Note
addBtn.addEventListener("click", function () {

    // Get text from textarea
    const noteText = noteInput.value.trim();

    // Don't allow empty notes
    if (noteText === "") {
        alert("Please write a note first!");
        return;
    }

    // Create a new note card
    const noteCard = document.createElement("article");

    // Create title
    const title = document.createElement("h2");
    title.textContent = "New Note";

    // Create note text
    const text = document.createElement("p");
    text.textContent = noteText;

    // Edit button
    const editBtn = document.createElement("button");
    editBtn.textContent = "Edit";

    // Delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";

    // Delete Function
    deleteBtn.addEventListener("click", function () {
        noteCard.remove();
    });

    // Edit Function
    editBtn.addEventListener("click", function () {

        const newText = prompt("Edit your note:", text.textContent);

        if (newText !== null && newText.trim() !== "") {
            text.textContent = newText;
        }

    });

    // Add everything to the card
    noteCard.appendChild(title);
    noteCard.appendChild(text);
    noteCard.appendChild(editBtn);
    noteCard.appendChild(deleteBtn);

    // Add card to page
    notesContainer.appendChild(noteCard);

    // Clear textarea
    noteInput.value = "";

});