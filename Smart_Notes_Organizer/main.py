print("\nPart 1: Preview Notes with read(n)")

file = open("classnotes2.txt", "r")
preview = file.read(40)
file.close()

print("First 40 charaters:")
print(preview)

print("\nPart 2: Read All Lines with readlines()")

file = open("classnotes2.txt", "r")
lines = file.readlines()


print("Total lines in file:", len(lines))

for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())

print("\nPart 3: Loop Through File line by line")

for line in file:
 file = open("Reading:", line.strip())


print("\nPart 4: Filter Lines with Conditions")

file = open("classnotes2.txt", "r")

for line in file:
   if line.startswith("SKIP"):
      print("Skipped", line.strip())
   else:
      print("Kept:", line.strip())



print("\nPart 5: Copy Selcted Lines to a new file")
file = open("classnotes2.txt", "r")
lines = file.readlines()
file.close

output_file = open("New Organized-notes.txt", "w")

for line in lines:
   if line.startswith("IMPORTANT" or line.startswith("TODO")):
      output_file.write(line)

output_file.close()

print("Selected lines copied to 'New Organized-notes.txt'.")

print("\nOrganized Notes:")

file = open("New Organized-notes.txt", "r")

for line in file:
   print(line.strip())

file.close()

print("\n================================")
print("SMART NOTES ORGANIZER SUMMARY")
print("\n================================")
print("read(n): Previewed the first few characters.")
print("readline(): Stored all lines in a list.")
print("Loop: Read the file line by line.")
print("Condition: Skipped Lines starting with SKIP.")
print("Copy: Saved IMPORTANT and TODO lines into a new file")
print("\n================================")
