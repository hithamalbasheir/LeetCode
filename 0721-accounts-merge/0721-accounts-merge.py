class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #initially, parents all nodes are parents to themselves
        parent = [i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(node):
            p = parent[node]
            #path compression
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(node1, node2):
            #Get parents of both nodes
            par1, par2 = find(node1), find(node2)

            #If both of them are already merged no need to keep going
            if par1 == par2:
                return False
            
            #The bigger one wins!
            if rank[par1] > rank[par2]:
                parent[par1] = parent[par2]
                rank[par1] += rank[par2]
            else:
                parent[par2] = parent[par1]
                rank[par2] += rank[par1]
            
            return True
        #a dict to store all emails linked to account index
        email_to_account = {}

        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in email_to_account:
                    union(i, email_to_account[email])
                email_to_account[email] = i
        
        res = defaultdict(list)
        for email, person in email_to_account.items():
            name = accounts[i][0]
            res[find(person)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]
