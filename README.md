# DiscordZ

Python GUI (Tkinter based) application that helps you choose between 2 discord profiles,
the profiles should be manually saved once be the user, then, the user can use this app to quickly switch profiles.

#### This app supports Windows ONLY (tested on 10, should work on 8.1)

profile switching is done by manipulating the directory structures under `%LOCALAPPDATA%\Discord`, `%APPDATA%\Discord`
this essentially changes the set of files used to save a discord login locally by the discord app

Profile storage location is hard-coded: `%USERPROFILE%\discord_profiles`
while discord is open, copy discord directories to `%USERPROFILE%\discord_profiles\main_profile` like this:

`%LOCALAPPDATA%\Discord` --> `%USERPROFILE%\discord_profiles\main_profile\Local\Discord`

`%APPDATA%\Discord` --> `%USERPROFILE%\discord_profiles\main_profile\Roaming\Discord`

after that, login to the alternative account and redo the copy using the other destination:

`%LOCALAPPDATA%\Discord` --> `%USERPROFILE%\discord_profiles\alt_profile\Local\Discord`

`%APPDATA%\Discord` --> `%USERPROFILE%\discord_profiles\alt_profile\Roaming\Discord`
