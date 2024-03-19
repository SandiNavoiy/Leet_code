class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Loop through each email in the given list of emails

        for i in range(len(emails)):
            # Split the email into local and domain parts based on '@' symbol
            temp = emails[i].split("@")
            x = ""

            # Iterate through each character in the local part of the email
            for j in temp[0]:
                if j == ".":
                    # If the character is a '.', skip it and continue
                    continue
                elif j == "+":
                    # If the character is '+', break the loop to ignore the rest of the local part
                    break
                else:
                    # Append characters to 'x' until encountering '+' or '.'
                    x += j

            # Update the email by modifying the local part and keeping the domain part unchanged
            emails[i] = x + "@" + temp[1]

        # Return the count of unique emails after modifying them
        return len(set(emails))
