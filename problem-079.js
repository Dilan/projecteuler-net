
var Node = function(id) {
    this.id = id;
    this.children = [];

    this.addChild = function(node) {
        this.children.push(node);
    };
};

var Report = function() {
    this.visited = {};
    this.sorted = [];

    this.isNotVisited = function(nodeId) {
        return ('undefined' == typeof this.visited[nodeId]);
    };

    this.markAsVisited = function(nodeId) {
        this.visited[nodeId] = true;
    };
}

var Net = function() {
    this.nodes = {};

    this.findById = function(id) {
        return (typeof this.nodes[id] == 'undefined') ? null : this.nodes[id];
    };

    this.createNode = function(id) {
        this.nodes[id] = new Node(id);
        return this.nodes[id];
    };
};

var createNet = function(edges) {
    return edges.reduce(function(net, edge) {
        var parentNodeId = edge[0],
            childNodeId = edge[1],

            initNode = function(id) {
                var node;
                if(null == (node = net.findById(id))) {
                    node = net.createNode(id);
                }
                return node;
            };

        initNode(parentNodeId).addChild(initNode(childNodeId));

        return net;

    }, new Net());
};

var visit = function(node, parents, report) {
    if(report.isNotVisited(node.id)) {
        report.markAsVisited(node.id);

        node.children.forEach(function(childNode) {
            if(parents.concat(node.id).indexOf(childNode.id) != -1) {
                throw new Error('Closed chain [ ' + childNode.id + ' -> ' + node.id + ' ]');
            }
            visit(childNode, parents.concat(node.id), report);
        });

        report.sorted.unshift(node.id);
    }
};

var topologicalSort = function(edges) {
    var report = new Report(),
        net = createNet(edges);

    Object.keys(net.nodes).forEach(function(nodeId) {
        // console.log('nodeId = ' + nodeId)
        visit(net.findById(nodeId), [], report);
    });
    return report.sorted;
};

var filePath = 'data/p079_keylog.txt'
require('fs').readFile(filePath, 'utf8', function (err, content) {
    var lines = content.split('\n');
    
    var edges = []
    lines.forEach(function(row) {
        if (!row) return
        var nums = row.split('');
        
        edges.push([nums[0], nums[1]])
        edges.push([nums[1], nums[2]])
        
    });
    console.log(topologicalSort(edges).join(''));
});

