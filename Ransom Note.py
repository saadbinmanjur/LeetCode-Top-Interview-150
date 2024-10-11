class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_hash = {}

        for c in magazine:
            m_hash[c] = 1 + m_hash.get(c, 0)
        
        for c in ransomNote:
            if c not in m_hash or m_hash[c] <= 0:
                return False
            m_hash[c] -= 1
        return True