class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_id = {}
        email_to_name = {}
        id_counter = 0
        
        # Step 1: Assign a unique integer ID to each unique email
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    email_to_name[email] = name
                    id_counter += 1
                    
        # Step 2: Initialize Union-Find structure
        uf = UnionFind(id_counter)
        
        # Step 3: Union emails inside the same account
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                uf.union(email_to_id[first_email], email_to_id[email])
                
        # Step 4: Group emails by their root parent ID
        from collections import defaultdict
        groups = defaultdict(list)
        for email, eid in email_to_id.items():
            root_id = uf.find(eid)
            groups[root_id].append(email)
            
        # Step 5: Format the final result
        result = []
        for root_id, emails in groups.items():
            # Get the name using any email from the group
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
            
        return result
