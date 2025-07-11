# Sakura Room

## TIP-OFF
### Answer the questions below

What username does the attacker go by?

Checking the page it says that you have been pwned

<img width="509" height="532" alt="image" src="https://github.com/user-attachments/assets/e5c65a01-25b3-46da-b365-54bb632e10f9" />

Viewing the page source we see that the image path has the username

<img width="864" height="142" alt="image" src="https://github.com/user-attachments/assets/1fddae0c-b862-414d-b45f-fed71f8aa246" />

**Answer**: SakuraSnowAngelAiko

## RECONNAISSANCE

### Answer the questions below

1. What is the full email address used by the attacker?

Searching the username in Google, we get Github and Twitter

Checking the Github, we see bunch of repositories

We will check the PGP repository as it contains the public key of the user

PGP, which stands for Pretty Good Privacy, is a widely used encryption program that provides both cryptographic privacy and authentication for data communication. It's primarily used to secure email communications, encrypt files, and digitally sign messages.

Copy and paste the public key through nano and create a file with `.asc` extension

An `.asc` file is a plain text file that uses the ASCII (American Standard Code for Information Interchange) character set. It's commonly used for storing various types of data, including messages, digital signatures, and even binary information encoded as text.

We can then extract the email address of the attacker by gpg command `gpg --import publicKey.asc`

<img width="798" height="142" alt="image" src="https://github.com/user-attachments/assets/104b7544-f5d6-45ac-9b4b-441cbca509dd" />

**Answer**: SakuraSnowAngel83@protonmail.com

2. What is the attacker's full real name?

By checking the Google, we get results like 6 Aiko Abe profile, so it confirms that the name is Aiko Abe as we get this by searching the username in Google

**Answer**: Aiko Abe

## UNVEIL

### Answer the questions below

1. What cryptocurrency does the attacker own a cryptocurrency wallet for?

From the Github profile, we see that there are 9 repositories

There is an ETH named repository that is a cryptocurrency used in Ethereum Virtual Machine

We see that there are 2 commits, Clicking on it gives us history of the commits

One is Update and other is Create, so the Create commit must contain the Cryptocurrency details

<img width="656" height="303" alt="image" src="https://github.com/user-attachments/assets/36318b21-911c-44ad-9e5b-427a4fd43946" />

<img width="975" height="216" alt="image" src="https://github.com/user-attachments/assets/3948ff2c-41a2-4536-b3d2-f08a90149023" />

**Answer**: Ethereum 

2. What is the attacker's cryptocurrency wallet address?

**Answer**: `0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef`

3. What mining pool did the attacker receive payments from on January 23, 2021 UTC?

As we know the cryptocurrency wallet address, we can see the public transactions

Checking any Blockchain Explorer in Internet and putting the address in the search bar

<img width="975" height="323" alt="image" src="https://github.com/user-attachments/assets/1a39ae69-95e2-4515-8e31-0d0d4bfa241f" />

We check in the Transactions through dates as we want on January 23, 2021

<img width="975" height="80" alt="image" src="https://github.com/user-attachments/assets/f280b692-e7e6-465d-9986-cf4476547cdc" />

**Answer**: Ethermine

4. What other cryptocurrency did the attacker exchange with using their cryptocurrency wallet?

Other than Ethereum we have Tether

<img width="975" height="79" alt="image" src="https://github.com/user-attachments/assets/3f2c140b-da3d-4548-8267-31c40e3c82b8" />

**Answer**: Tether

## TAUNT

### Answer the questions below

1. What is the attacker's current Twitter handle?

By searching the username in Google, we get the Twitter 

<img width="942" height="451" alt="image" src="https://github.com/user-attachments/assets/09f06b01-647d-4e73-b09a-e127c4e7e0b2" />

**Answer**: SakuraLoverAiko

2. What is the BSSID for the attacker's Home WiFi?

We see a post of WiFi and password as hash and hinting us that the information is kept DEEP meaning hidden in Dark web as Onion website Deep Paste

Using the Tor Browser and searching the hash in Deep Paste

<img width="650" height="304" alt="image" src="https://github.com/user-attachments/assets/02aa4046-053d-4f8b-857a-1cb44b406547" />

We get the Home WiFi name which is SSID as DK1F-G

SSID stands for Service Set Identifier. It is the name of your Wi-Fi network, used to identify and distinguish it from other nearby networks.

Putting the SSID in Wigle.net to get the BSSID

Put the SSID in Advanced Search we get one result

<img width="623" height="273" alt="image" src="https://github.com/user-attachments/assets/83fac90d-55ce-4250-a3b0-54b463c43984" />

Answer: `84:AF:EC:34:FC:F8`

## HOMEBOUND

### Answer the questions below

1. What airport is closest to the location the attacker shared a photo from prior to getting on their flight?

Seeing the tweet, saving the image

<img width="929" height="532" alt="image" src="https://github.com/user-attachments/assets/eec5a12d-ea74-4405-b0a5-94392389dc20" />

Searching nearby airport in Google by uploading the image

<img width="975" height="504" alt="image" src="https://github.com/user-attachments/assets/dd93f910-fd41-403c-a0f6-f3d19dddf563" />

**Answer**: DCA

2. What airport did the attacker have their last layover in?

Seeing the tweet that the place attacker has been lately

<img width="939" height="589" alt="image" src="https://github.com/user-attachments/assets/5ec0ffd3-9f6c-45db-ba64-1544544df68a" />

Saving the image and searching it in Google the aiport that has this lounge

In the About image we can see an article hinting Haneda HND

<img width="975" height="273" alt="image" src="https://github.com/user-attachments/assets/9342a700-1785-404b-8121-e683512f006d" />

**Answer**: HND

3. What lake can be seen in the map shared by the attacker as they were on their final flight home?

Seeing the tweet likely a map, saving the image and searching the lake in Google

<img width="948" height="642" alt="image" src="https://github.com/user-attachments/assets/7e848197-14e9-4e5b-a489-27ff55f51286" />

<img width="500" height="375" alt="image" src="https://github.com/user-attachments/assets/5b410d63-6215-4bdd-99e6-79a7fb029fb5" />

**Answer**: Lake Inawashiro

4. What city does the attacker likely consider "home"?

As the tweet says that it is close so it must be heading north

As we know the lake Inawashiro and the SSIDs we found from the dark web

We founded SSIDs of Home Wifi, School Wifi and City Free Wifi so it will result in the same city

The City Free Wifi is HIROSAKI_FREE-Wi-Fi in which Hirosaki is a city name in Japan

<img width="939" height="801" alt="image" src="https://github.com/user-attachments/assets/4128360e-1dc3-434a-8d5f-49555cfcacb8" />
