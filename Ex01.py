# Maak volgende lists aan:
# - Een list met de drie klasgroepen in MCT
# - Een list met de twee klasgroepen in CTAI
# Print beide lists af.
# MCT heeft volgende klasgroepen in het eerste jaar: ['1MCT1', '1MCT2', '1MCT3']
# CTAI heeft volgende klasgroepen in het eerste jaar: ['1CTAI1', '1CTAI2']
# Kan je twee lists met elkaar optellen? Test uit door de som af te printen.

klasgroepen_mct = ["1MCT1", "1MCT2", "1MCT3"]
klasgroepen_ctai = ["1CTAI1","1CTAI2"]

print(f"MCT heeft de klasgroepen {klasgroepen_mct}")
print(f"CTAI heeft de klasgroepen {klasgroepen_ctai}")
#de som van 2 lists levert een nieuwe list op, waarin alle elementen samen zitten
print(f"Alle groepen samen: {klasgroepen_ctai + klasgroepen_mct}")