
d3.text("mindmap.data").then(function (text) {
    let nodes = [];
    let links = [];
    let lines = text.split("\n");

    lines.forEach(function (line) {
        // Ignore empty lines
        if (line.trim() === '') {
            return;
        }
        let parts = line.split(" -- ");
        let source = parts[0];
        let target = parts[1];

        if (!nodes.find(node => node.id === source)) {
            nodes.push({ id: source, group: 1 });
        }

        if (!nodes.find(node => node.id === target)) {
            nodes.push({ id: target, group: 1 });
        }

        links.push({ source: source, target: target });
    });


    let svg = d3.select("svg"),
        width = +svg.attr("width"),
        height = +svg.attr("height");

    let simulation = d3.forceSimulation(nodes)
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("link", d3.forceLink(links).id(d => d.id).distance(100).strength(1))
        .force("charge", d3.forceManyBody().strength(-1000))
        .force("x", d3.forceX())
        .force("y", d3.forceY());

    let link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(links)
        .enter().append("line")
        .attr("stroke", "black");

    let node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(nodes)
        .enter().append("circle")
        .attr("r", 5)
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    let label = svg.append("g")
        .attr("class", "labels")
        .selectAll("text")
        .data(nodes)
        .enter().append("text")
        .attr("class", "label")
        .text(function (d) { return d.id; });

    nodes = nodes;
    links = links;


    simulation
        .nodes(nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(links);

    function ticked() {
        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        label
            .attr("x", function (d) { return d.x + 10; })
            .attr("y", function (d) { return d.y + 10; });
    }

    function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended(d) {
        if (!d3.event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

    d3.select("#charge-strength").on("input", function () {
        simulation.force("charge").strength(+this.value);
        simulation.alpha(1).restart();
    });

});
