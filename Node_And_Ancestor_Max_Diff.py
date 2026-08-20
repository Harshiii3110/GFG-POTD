        ans = [float('-inf')]

        def dfs(node, max_ancestor):
            if node is None:
                return

            # Compare current node with its ancestor
            if node != root:
                ans[0] = max(ans[0], max_ancestor - node.data)

            # Current node can become an ancestor for its children
            max_ancestor = max(max_ancestor, node.data)

            dfs(node.left, max_ancestor)
            dfs(node.right, max_ancestor)

        dfs(root, root.data)

        return ans[0]
