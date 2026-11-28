class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # Split both strings into lists of revision strings
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Iterate up to the length of the longer version list
        max_len = max(len(v1), len(v2))
        
        for i in range(max_len):
            # Convert to int (automatically removes leading zeros)
            # Default to 0 if one version has fewer revisions
            rev1 = int(v1[i]) if i < len(v1) else 0
            rev2 = int(v2[i]) if i < len(v2) else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
                
        return 0
