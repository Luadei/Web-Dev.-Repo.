const cardGroup = document.querySelector(".row")

const writeCards = (project) => {
	cardGroup.innerHTML += `
        <div class="col">
            <div class="card">
                <img src="assets/proj-imgs/${
									project.imageUrl
								}" class="card-img-top" alt="..." />
                <div class="card-body">
                    <h3 class="card-title">${project.title}</h3>
                    <p class="card-text">${project.description}</p>
                    <div class="btn-group btn-group-sm" role="group" aria-label="Basic outlined example">
                        <a href="${
													project.links[0]
												}" target="_blank" class="btn btn-outline-dark">
                                <img src="./assets/code.svg" >
                        </a>
                        <a href="${
													project.links[1]
												}" target="_blank" class="btn btn-outline-dark">
                                <img src="./assets/server.svg" >
                        </a>
                    </div>   
                </div>
                <div class="card-footer">
                    <h3 class="h6">Technologies</h3>
                    <div class="d-flex justify-content-evenly p-2">
                        ${writeTechnologies(project.technologies)}
                    </div>
                </div>
            </div>
        </div>
    `
}

const writeTechnologies = (technologies) => {
	let html = ""
	technologies.forEach((techno) => {
		html += `<span class="badge bg-secondary">${techno}</span>`
	})
	return html
}

projects.forEach((project) => {
	writeCards(project)
})
