import clr


clr.AddReference("dlls/PrefixesLib")
from PrefixesLib import PrefixManager



prefix_manager = PrefixManager()

print("Po dodaniu 3 pętla \n");

prefix_manager.Add(16909060, ' ')
prefix_manager.Add(16909060, '\x01')
prefix_manager.Add(16909060, '\x05')
prefix_manager.Add(16909, '\x06')

for i in range(prefix_manager.prefixSet.Size):
    prefix = prefix_manager.prefixSet.Prefixes[i]
    print("Base:", prefix.Base, "Mask:", ord(prefix.Mask))

prefix_manager.Delete(16909060, ' ')

print("JEDEN USNIĘTY \n");
for i in range(prefix_manager.prefixSet.Size):
    prefix = prefix_manager.prefixSet.Prefixes[i]
    print("Base:", prefix.Base, "Mask:", ord(prefix.Mask))

max_mask = prefix_manager.Check(16909060)
print("Największa maska:", max_mask)