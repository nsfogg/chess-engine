import unittest
import tree_mod

class TestTree(unittest.TestCase):
    def test_create(self):
        tree = tree_mod.TreeNode(1)
        self.assertEqual(tree.data, 1, "Should be 1")
        self.assertEqual(tree.children, [], "Should be empty")
        self.assertEqual(tree.parent, None, "Should be None")
    
    def test_add_children(self):
        root = tree_mod.TreeNode("a")
        b = tree_mod.TreeNode("b")
        root.add_child(b)
        c = tree_mod.TreeNode("c")
        root.add_child(c)

        self.assertEqual(root.children[0], b, "Should be b")
        self.assertListEqual(root.children, [b, c], "Should be [b, c]")

        d = tree_mod.TreeNode("d")
        b.add_child(d)
        self.assertEqual(root.children[0].children[0], d, "Should be d")
    
    def test_get_level(self):
        root = tree_mod.TreeNode(0)
        a = tree_mod.TreeNode(1)
        b = tree_mod.TreeNode(2)
        c = tree_mod.TreeNode(3)
        
        root.add_child(a)
        a.add_child(b)
        b.add_child(c)

        self.assertEqual(root.get_level(), 0, "Should be 0")
        self.assertEqual(a.get_level(), 1, "Should be 1")
        self.assertEqual(b.get_level(), 2, "Should be 2")
        self.assertEqual(c.get_level(), 3, "Should be 3")


if __name__ == '__main__':
    unittest.main()