# BAS-IP API — все методы (актуальные версии)

## android-monitors — current (77 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| GET | `/advanced/announcement` | Returns the announcement settings. When enabled, the announcement URL  | advanced |
| POST | `/advanced/announcement` | Configures the announcement settings. When enabled, the announcement U | advanced |
| GET | `/advanced/announcement/run` | Immediately triggers the announcement playback. | advanced |
| POST | `/advanced/browser` | Configures the site URLs displayed in the `Service` app. | advanced |
| POST | `/advanced/elevator/modules` | Configures elevator module indexes. Send an empty `items` array to set | advanced |
| PUT | `/advanced/emergency/{emergency-id}/settings` | Update settings for the emergency alarm.  If the alarm with the specif | advanced |
| PUT | `/advanced/emergency/{emergency-id}/sound` | Upload a WAV audio file for the emergency alarm.  If the alarm with th | advanced |
| POST | `/advanced/emergency/{emergency-id}/stop` | Stop playback of the emergency alarm.  | advanced |
| GET | `/advanced/standby` | Returns standby settings.  Standby mode is a splash screen displayed w | advanced |
| DELETE | `/contacts` | Deletes contacts by the specified IDs, or clears all contacts if no ID | contact |
| GET | `/contacts` | Returns the list of all contacts. | contact |
| DELETE | `/contacts/recents` | Removes all recent call records from the contact book. | contact |
| DELETE | `/contacts/{entity-uid}` | Deletes the specified contact. | contact |
| POST | `/desktop/logo` | Uploads a logo image for the desktop. Any image format and resolution  | desktop |
| GET | `/device/time` | Returns the current device time (Unix timestamp) and timezone. | status |
| GET | `/intercom/advanced` | Returns the current state of advanced intercom call options:  - `camer | intercom |
| POST | `/intercom/advanced/autoanswer` | Configures the auto answer feature.  When enabled, plays a "nobody hom | intercom |
| POST | `/intercom/advanced/autohungup` | Configures the auto hang-up feature. When enabled, the call is automat | intercom |
| POST | `/intercom/advanced/camera` | Enables or disables the device camera during calls. | intercom |
| POST | `/intercom/advanced/protectunlock` | Configures the protect unlock feature. When enabled, a login dialog is | intercom |
| GET | `/intercom/dtmf` | Returns the DTMF key settings used for opening the door lock during a  | intercom |
| GET | `/intercom/exphone` | Returns the extended phone settings. When enabled, incoming calls are  | intercom |
| POST | `/intercom/exphone` | Configures the extended phone settings. When enabled, incoming calls a | intercom |
| GET | `/intercom/multicast/paging` | Get multicast paging settings | intercom |
| POST | `/intercom/multicast/paging` | Set multicast paging settings | intercom |
| GET | `/intercom/room` | Returns the logical address of the device. The logical address defines | intercom |
| POST | `/intercom/room` | Configures the logical address of the device. The logical address defi | intercom |
| GET | `/intercom/sip` | Returns the SIP (Session Initiation Protocol) account settings. | intercom |
| POST | `/intercom/sip` | Configures the SIP (Session Initiation Protocol) account settings. | intercom |
| GET | `/intercom/sos` | Returns the SOS button configuration, including the target SIP number  | intercom |
| POST | `/language` | Sets the current system language. | status |
| DELETE | `/link/announcements` | Deletes announcements by their IDs. | link |
| GET | `/link/announcements` | Returns the list of announcements (polls and info messages) received f | link |
| GET | `/login` | Authenticates a user and returns a Bearer token for subsequent request | auth |
| GET | `/main/dnd` | Returns the Do Not Disturb (DND) settings.  There are two modes:   - S | main |
| GET | `/network/dst` | Returns Daylight Saving Time (DST) settings.  DST is a seasonal time c | network |
| POST | `/network/dst` | Configures DST settings.  DST is a seasonal time change measure where  | network |
| GET | `/network/link` | Returns the remote Link server configuration.  This endpoint is deprec | link,network |
| POST | `/network/link` | Configures remote Link server settings.  This endpoint is deprecated.  | link,network |
| GET | `/network/management/server` | Returns the management server configuration.  If Link is enabled, the  | network,link |
| DELETE | `/network/management/server/certificate` | Removes the uploaded certificate for the management server MQTT connec | network,link |
| GET | `/network/management/server/certificate` | Returns whether a custom certificate has been uploaded for the managem | network,link |
| GET | `/network/ms` | Returns the Remote Management Software (RMS) server URL and password. | link,network |
| POST | `/network/ms` | Configures the Remote Management Software (RMS) server URL and passwor | link,network |
| POST | `/network/ntp` | Configures NTP settings. | network |
| GET | `/network/settings` | Returns Ethernet interface settings. If DHCP is enabled, the response  | network |
| POST | `/network/settings` | Configures Ethernet interface settings.  Note: DHCP cannot be enabled  | network |
| GET | `/network/sipnet` | Returns the current network interface configuration used for SIP traff | intercom,network |
| POST | `/network/timezone` | Sets the device timezone. NTP must be enabled. | network |
| GET | `/network/wifi/connection` | Returns information about the current Wi-Fi connection. | network,wifi |
| POST | `/network/wifi/connection` | Connects to a Wi-Fi network using the provided SSID and password. If t | network,wifi |
| GET | `/network/wifi/saved-networks` | Returns a list of previously saved Wi-Fi networks. | network,wifi |
| POST | `/network/wifi/settings/static` | Configures static IP settings for the Wi-Fi interface and disables DHC | network,wifi |
| GET | `/security/monitors/sos` | Get SOS monitor configuration.  Only a single monitor number is suppor | security |
| GET | `/security/nowip` | Returns the NowIP alarm notification settings.  NowIP provides additio | security |
| GET | `/security/scene` | Returns the security scene settings.  Three scenes are available: Out, | security |
| POST | `/security/scene` | Configures the security scene settings.  Three scenes are available: O | security |
| POST | `/security/whitelist` | Removes the specified IP addresses from the login whitelist. | security,auth |
| PUT | `/security/whitelist` | Adds the specified IP addresses to the login whitelist. | security,auth |
| GET | `/security/zone` | Returns the security sensor (zone) settings.  - **No** — zone number.  | security |
| GET | `/sip/status` | Returns the current SIP registration status. Available statuses:   * ` | status |
| GET | `/system/concierge/forward` | Returns the multiple-concierge call mode settings. | concierge |
| POST | `/system/concierge/forward` | Configures the multiple-concierge call mode feature. Enabling this fea | concierge |
| DELETE | `/system/debug/log` | Clears all system logs stored on the device. | system,debug |
| GET | `/system/debug/log` | Returns a password-protected ZIP file containing the device system log | system,debug |
| GET | `/system/firmware/check` | Returns information about the latest available firmware version from t | system |
| POST | `/system/firmware/update/cloud` | Starts the firmware update process using the latest version from the c | system |
| GET | `/system/firmware/updates` | Returns the firmware update settings, including automatic update check | system |
| POST | `/system/firmware/updates` | Configures the firmware update settings, including automatic update ch | system |
| POST | `/system/password/admin` | Changes the administrator password. | security |
| POST | `/system/password/user` | Changes the user password.  The user password is required to save cert | security |
| GET | `/system/reboot` | Reboots the device. | system |
| GET | `/system/rtsp` | Returns the RTSP feed stream URLs configured for AM-02 devices. | concierge |
| POST | `/system/rtsp` | Configures the RTSP feed stream URLs for AM-02 devices. Each stream mu | concierge |
| GET | `/system/settings/backup` | Returns a backup ZIP file containing all device settings. | system |
| POST | `/system/settings/file` | Applies device settings from a previously exported backup file. | system |
| POST | `/timezone` | Sets the device timestamp and timezone. NTP must be disabled to set a  | status |

## android-panels — current (230 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| GET | `/access/auth/factors` | Used to get available auth factors. AV-08FB and BI panels do not suppo | access,admin |
| GET | `/access/exit/button/toggle` | Returns status of the contacts of the exit button. If disabled, the do | access,admin |
| GET | `/access/external/control` | Returns info external control availability | access |
| POST | `/access/freeaccess` | - Create Free access Time Profile - Provides free access on proper sch | access,admin |
| DELETE | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| GET | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| POST | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| GET | `/access/general/elevator/floor` | This endpoint is deprecated, use `GET /access/general/elevator/setting | access,admin |
| POST | `/access/general/elevator/floor` | This endpoint is deprecated, use `GET /access/general/elevator/setting | access,admin |
| POST | `/access/general/emergency/toggle` | Activates emergency alarm on device | system |
| GET | `/access/general/facerecognition` | Get face recognition settings. This feature is available on devices wi | access,admin |
| POST | `/access/general/lock/delay/{single-lock-number}` | Time delay before panel relay contacts will be open | access,admin |
| POST | `/access/general/lock/dtmf/{lock-number}` | Configure DTMF code used for opening lock during call  `DTMF code rege | access,admin |
| POST | `/access/general/lock/open/emergency` | Open the locks in emergency mode for a specified duration. The unlock  | access,admin |
| GET | `/access/general/lock/open/remote/control/accepted/{lock-number}` | Opens lock and trigger "access allowed" event via HTTP (for Remote Acc | access,admin |
| GET | `/access/general/lock/timeout/{single-lock-number}` | Returns time for which the relay contacts will be closed after opening | access,admin |
| GET | `/access/general/lock/type` | Gets the type of lock used:   - electromagnetic   - electromechanical  | access,admin |
| POST | `/access/general/lock/type` | Set the type of lock used:   - electromagnetic   - electromechanical | access,admin |
| GET | `/access/general/qr` | Returns QR feature setting. - If enabled QR code can be used to unlock | access,admin |
| GET | `/access/general/security/monitor` | If the feature is enabled, then when the card brought to the reader th | access,admin |
| POST | `/access/general/security/monitor` | If the feature is enabled, then when the card brought to the reader th | access,admin |
| GET | `/access/general/unlock/card/master` | Get master card number. - Master card can be used to add another cards | access,admin |
| POST | `/access/general/unlock/card/master` | Set master card number. - Master card can be used to add another cards | access,admin |
| GET | `/access/general/unlock/input/code` | Get master access code and feature status. Available only on panels wi | access,admin |
| POST | `/access/general/wiegand` | Configures Wiegand input/output.  Wiegand type. All data received on W | access,admin |
| GET | `/access/general/wiegand/type` | Gets the type of Wiegand used for internal card reader.  | access,admin |
| POST | `/access/general/wiegand/type` | Setting up the type of Wiegand used for internal card reader.  | access,admin |
| POST | `/access/global/settings` | Used to set information about current global access settings.  To enab | access,admin |
| POST | `/access/identifier` | Create Identifier Entity. You can create identifiers with the next typ | access,admin |
| DELETE | `/access/identifier/item/{identifier-uid}` | Delete Identifier Entity | access,admin |
| GET | `/access/identifier/item/{identifier-uid}` | Returns detailed info about Identifier | access,admin |
| POST | `/access/identifier/item/{identifier-uid}/passes/reset` | Reset left passes to max, if there is a restriction on the number of p | access,admin |
| GET | `/access/identifier/item/{identifier-uid}/qr` | Returns png representation of the stored QR identifier | access,admin |
| DELETE | `/access/identifier/item/{identifier-uid}/timeprofile/{timeprofile-uid}` | Detach Time Profile from Identifier | access,admin |
| POST | `/access/identifier/item/{identifier-uid}/timeprofile/{timeprofile-uid}` | Attach Time Profile rule to Identifier | access,admin |
| DELETE | `/access/identifier/items` | Delete multiple Identifier items | access,admin |
| GET | `/access/identifier/items` | Returns identifiers list with options could be used to sort and filter | access,admin |
| DELETE | `/access/identifier/items/link` | Delete multiple Identifier items by `link_id` param. This request is u | access,admin,link |
| GET | `/access/identifier/items/link` | Get multiple Identifier items with `link_id`.  This can be used by 3d- | access,admin,link |
| POST | `/access/identifier/items/link` | Create or Update multiple Identifier items.  This request is used by ` | access,admin,link |
| GET | `/access/lift` | Returns KONE lift adapter, required for interaction with KONE module  | access,admin |
| POST | `/access/lift` | Configures KONE lift adapter, required for interaction with KONE modul | access,admin |
| GET | `/access/lift/rules` | Returns detailed info about all Access Rule | access,admin |
| POST | `/access/lift/rules` | Creates Access Rule Entity.  Access rule provides access for proper *a | access,admin |
| DELETE | `/access/lift/rules/link` | This request is used by Link management system to delete Access Rules  | access,admin,link |
| GET | `/access/lift/rules/link` | Returns detailed info about Access Rules | access,admin,link |
| POST | `/access/lift/rules/link` | Bulk Access Rule Entity creation/updating.  Access rule provides acces | access,admin,link |
| DELETE | `/access/lift/rules/{rule-uid}` | Deletes Access Rule Entity | access,admin |
| GET | `/access/lift/rules/{rule-uid}` | Returns detailed info about Access Rule | access,admin |
| PUT | `/access/lift/rules/{rule-uid}` | Updates Access Rule Entity | access,admin |
| GET | `/access/lift/topology` | Returns available area in the building.  To get topology KONE lift mod | access,admin |
| DELETE | `/access/lift/zones` | Delete Access Zone items by uid | access,admin |
| GET | `/access/lift/zones` | Returns detailed info about all Access Zones | access,admin |
| GET | `/access/lift/zones/relations` | Returns list of entities connected with BOND access zones  | access,admin |
| GET | `/access/lift/zones/settings` | Returns BOND lift settings  BOND lift cannot work simultaneously with  | access,admin |
| POST | `/access/lift/zones/settings` | Configures BOND lift adapter, required for interaction with BOND modul | access,admin |
| PUT | `/access/lift/zones/{zone-uid}` | Updates Access Zone Entity | access,admin |
| DELETE | `/access/lift/zones/{zone-uid}/relations` | Detaches access zone from identifier or call number.  | access,admin |
| POST | `/access/lift/zones/{zone-uid}/relations` | Attaches access zone to identifier or call number.  Access zone provid | access,admin |
| POST | `/access/parking/terminal` | Opens first relay if access granted, and second if access denied. Supp | access,admin |
| GET | `/access/timeprofile/item/{timeprofile-uid}` | Returns Time Profile Entity | access,admin |
| PATCH | `/access/timeprofile/item/{timeprofile-uid}` | Update Time Profile Entity | access,admin |
| DELETE | `/access/timeprofile/items` | Delete Time Profile items by uid | access,admin |
| GET | `/access/timeprofile/items` | Returns Time Profiles list | access,admin |
| DELETE | `/access/timeprofile/items/link` | Delete multiple Time Profile items by `link_id` param. This request is | access,admin,link |
| PUT | `/access/user` | Creates user entity  | access,admin |
| DELETE | `/access/user/identifier/{identifier-uid}` | Allows to detach identifier from user | access,admin |
| DELETE | `/access/user/item/{user-uid}` | Deletes User Entity | access,admin |
| GET | `/access/user/item/{user-uid}` | Returns detailed info about User | access,admin |
| POST | `/access/user/items/link` | Create/update multiple User Entities with `link_id`.  If entity doesn' | access,admin,link |
| POST | `/access/user/{user-uid}/identifier/{identifier-uid}` | Allows to attach identifier to user | access,admin |
| DELETE | `/access/user/{user-uid}/timeprofile/{timeprofile-uid}` | Allows to detach timeprofile from user | access,admin |
| POST | `/access/user/{user-uid}/timeprofile/{timeprofile-uid}` | Allows to attach timeprofile to user | access,admin |
| GET | `/access/users/{user-uid}/lift/rules` | Returns detailed info about all Access Rule attached to user | access,admin |
| DELETE | `/advanced/announcement/standby/media` | Removes media file uploaded on device.  | advanced,admin |
| POST | `/advanced/announcement/standby/media` | - Add or update media file, used for displaying in standby.  Supports  | advanced,admin |
| DELETE | `/advanced/notification/button/press/sound` | Removes buttons press custom sound. Device will use default sound. | advanced,manager |
| GET | `/advanced/notification/button/press/sound` | Returns buttons press custom sound settings | advanced,manager |
| PATCH | `/advanced/notification/button/press/text` | The text displayed on the panel main screen can be customized, for exa | advanced,manager |
| GET | `/advanced/notification/call-start` | Returns start call sound state information | advanced,manager |
| POST | `/advanced/notification/call-start` | Enable/Disable start call sound feature | advanced,manager |
| PATCH | `/advanced/notification/call-start/sound` | Uploads custom start call sound file | advanced,manager |
| POST | `/advanced/notification/call-start/sound` | Enable/Disable custom start call sound feature | advanced,manager |
| GET | `/advanced/notification/conversation-start` | Returns conversation start sound state information | advanced,manager |
| POST | `/advanced/notification/conversation-start` | Enable/Disable conversation start sound feature | advanced,manager |
| GET | `/advanced/notification/conversation-start/sound` | Returns custom conversation start sound settings | advanced,manager |
| PATCH | `/advanced/notification/conversation-start/sound` | Uploads custom conversation start sound file | advanced,manager |
| GET | `/advanced/notification/emergency/sound` | Returns custom emergency sound settings | advanced,manager |
| PATCH | `/advanced/notification/emergency/sound` | Uploads custom emergency sound file | advanced,manager |
| POST | `/advanced/notification/emergency/sound` | Enable/Disable custom emergency sound feature | advanced,manager |
| GET | `/advanced/notification/emergency/text` | Returns settings of emergency custom text | advanced,manager |
| PATCH | `/advanced/notification/emergency/text` | Setup custom error notification text | advanced,manager |
| PATCH | `/advanced/notification/error/sound` | Uploads custom error sound file | advanced,manager |
| POST | `/advanced/notification/error/sound` | Enable/Disable custom error sound feature | advanced,manager |
| GET | `/advanced/notification/error/text` | Returns settings of error custom text | advanced,manager |
| PATCH | `/advanced/notification/error/text` | Set error custom text value | advanced,manager |
| POST | `/advanced/notification/error/text` | Enable/Disable error custom text | advanced,manager |
| PATCH | `/advanced/notification/lock/open/sound` | Uploads custom lock open sound file | advanced,manager |
| POST | `/advanced/notification/lock/open/sound` | Enable/Disable custom lock open sound feature | advanced,manager |
| POST | `/advanced/notification/lock/open/text` | Enable/Disable lock open custom text | advanced,manager |
| DELETE | `/advanced/notification/progress/sound` | Removes custom external access sound | advanced,manager |
| GET | `/advanced/notification/progress/sound` | Returns custom external access sound settings | advanced,manager |
| GET | `/advanced/notification/progress/text` | Returns settings of external access custom text | advanced,manager |
| POST | `/advanced/notification/progress/text` | Enable/Disable external access custom text | advanced,manager |
| GET | `/advanced/notification/recognition/hints` | Get information about face/QR recognition voice hints status. This fea | advanced |
| POST | `/advanced/notification/recognition/hints` | Enable/disable face/QR recognition voice hints. This feature is availa | advanced |
| GET | `/advanced/notification/ringing/tone/sound` | Returns custom ringing tone settings | advanced,manager |
| PATCH | `/advanced/notification/ringing/tone/text` | Set ringing status custom text value on the call screen | advanced,manager |
| POST | `/advanced/notification/ringing/tone/text` | Enable/Disable ringing status custom text | advanced,manager |
| POST | `/advanced/rtsp/feed` | The function of viewing additional IP cameras during a call (up to 4 s | advanced,manager |
| POST | `/apartment` | Creates Apartment Entity. The `uid` value returned in the response can | apartment,admin |
| GET | `/apartment/book` | Get apartment phone book feature status. * When feature enabled, apart | apartment,admin |
| DELETE | `/apartment/item/unbind/identifier/{identifier-uid}` | Delete a relation between the identifier and the apartment entities | apartment,admin |
| DELETE | `/apartment/item/{apartment-uid}` | Delete Apartment Entity and removes detaches all identifiers attached  | apartment,admin |
| GET | `/apartment/item/{apartment-uid}` | Returns Apartment Entity detailed information.  Base Apartment Entity  | apartment,admin |
| POST | `/apartment/item/{apartment-uid}/identifier/{identifier-uid}` | Create a relation between the identifier and the apartment entities.   | apartment,admin |
| DELETE | `/apartment/item/{apartment-uid}/route` | - Delete Apartment Entity route image - This feature is available only | apartment,admin |
| POST | `/apartment/item/{apartment-uid}/route` | - Upload Apartment Entity route image - This feature is available only | apartment,admin |
| DELETE | `/apartment/item/{apartment-uid}/user/{user-uid}` | Allows to detach user from apartment | access,admin |
| POST | `/apartment/item/{apartment-uid}/user/{user-uid}` | Allows to add user to apartment | access,admin |
| DELETE | `/apartment/items` | Delete multiple apartment items by their IDs | apartment,admin |
| GET | `/apartment/items` | Return Apartments entities detailed list with used pagination, filter  | apartment,admin |
| DELETE | `/apartment/items/link` | Delete multiple Apartment Entities with `link_id`.  If apartment with  | apartment,admin,link |
| POST | `/apartment/routes/backup` | - Imports all apartment route image files from zip archive. The device | apartment,admin |
| DELETE | `/companies` | Deletes multiple Companies | admin,company |
| GET | `/companies` | - Returns a list of Companies with options could be used to sort and f | admin,company |
| POST | `/companies` | Creates Company Entity. The `item_uid` value returned in the response  | admin,company |
| GET | `/companies/{company-uid}` | - Returns information about Company and attached Apartments. - This fe | admin,company |
| POST | `/companies/{company-uid}/apartments/{apartment-uid}` | Allows to attach Apartment to Company. Many Apartment can be attached  | company,apartment,admin |
| DELETE | `/companies/{company-uid}/logo` | - Removes Company image profile photo. - This feature is available onl | admin,company |
| DELETE | `/desktop/button/item/icon` | Resets desktop app icon to default - This feature is available only in | desktop,admin |
| POST | `/desktop/button/items` | Enables or disables application on desktop  - This feature is availabl | desktop,manager |
| GET | `/desktop/button/preview` | Returns screenshot image file. This endpoint is used for configuring c | desktop,manager |
| POST | `/desktop/message` | Show message in the desktop notifications list - This feature is avail | desktop,admin |
| DELETE | `/desktop/message/item/{message-uid}` | Delete message from the desktop notifications list by uid - This featu | desktop |
| DELETE | `/desktop/message/items` | Delete all messages from the desktop notifications list by uid - This  | desktop,admin |
| DELETE | `/desktop/message/items/link` | This request is used by Link management system to delete messages by ` | desktop,link,admin |
| GET | `/desktop/statusbar` | Returns a text displayed in the toolbar on the main screen, for exampl | desktop,admin |
| POST | `/desktop/statusbar` | Set a text displayed in the toolbar on the main screen, for example, a | desktop |
| DELETE | `/desktop/wallpaper` | Reset wallpaper to default - This feature is available only on devices | desktop,admin |
| GET | `/desktop/wallpaper` | Returns wallpapers image URI which can be used to retrieve file. - Thi | desktop,admin |
| GET | `/device/call/concierge` | Configure concierge number settings. * If enabled panel will call to p | device,manager |
| POST | `/device/call/concierge` | Configure concierge number settings. * If enabled panel will call to p | device,manager |
| GET | `/device/call/dial/auto` | The function of automatic dialing after entering the number digits spe | device,manager |
| POST | `/device/call/dial/auto` | The function of automatic dialing after entering the number digits spe | device,manager |
| GET | `/device/call/dial/timeout` | Returns time interval after which the panel automatically ends an outg | device,manager |
| POST | `/device/call/dial/timeout` | A time interval after which the panel automatically ends an outgoing c | device,manager |
| POST | `/device/call/drop` | Set current settings for dropping call after second button press, this | device |
| GET | `/device/call/hungup` | Automatically end the call after opening the door with exit button if  | device,admin |
| GET | `/device/call/talk/bidirectional` | Enables user-to-user video communication during outgoing call. A black | device,manager |
| POST | `/device/call/talk/bidirectional` | Enables user-to-user video communication during outgoing call. A black | device,manager |
| POST | `/device/call/talk/timeout` | Set the time interval after which the panel automatically ends the out | device,manager |
| GET | `/device/control4/settings` | Get the settings for integration with `Control4`. - Not available on C | admin,integration,control4 |
| POST | `/device/control4/settings` | Set the settings for integration with `Control4`. - Not available on C | admin,integration,control4 |
| GET | `/device/language` | Get current system language and the list of supported languages | status |
| POST | `/device/language` | Set current system language | status,manager |
| POST | `/device/mode/apartment` | Set panel work mode to `Apartment` mode - `Apartment` mode is unique m | device |
| POST | `/device/mode/wall` | Set panel work mode to `Wall` mode. - In `Wall` mode you must enter fu | device,manager |
| POST | `/device/relay/settings` | Configure relay inversion settings. If inverted start relay position w | device,admin |
| POST | `/device/screen/brightness` | Set current device brightness level. Min is 0 and max is 100 | device |
| GET | `/device/security/tamper` | - Returns current tamper settings     - This options are available for | security,system |
| POST | `/device/security/tamper` | - Turns on/off tamper - This options are available for all devices exc | security,system |
| GET | `/device/sensor/proximity` | Returns proximity sensor setting - It wakes up screen when triggered - | device,admin |
| POST | `/device/sensor/proximity` | - Configures proximity sensor settings. There are two modes: *adaptive | device,admin |
| POST | `/device/settings/ir` | The endpoint is deprecated, use `POST /device/proximity/sensor`  Turn  | device,manager |
| GET | `/device/settings/led` | Returns LED auto mode settings | device,manager |
| GET | `/device/settings/payload` | Returns information about video Real-time Transport Protocol (RTP) pro | device,manager |
| POST | `/device/settings/rtsp` | Set **username**, **password** and audio enabled used to access panel' | device,manager |
| POST | `/device/settings/rtsp/timestamp` | Configures RTSP timestamp mark displaying options  | device,admin |
| GET | `/device/settings/video` | Returns camera video resolution, frame rate, bitrate (only in AA-FBS,  | device,manager |
| GET | `/device/settings/volume` | Returns speaker volume level | device,manager |
| POST | `/device/sip/enable` | Turns On/Off calls with Session Initiation Protocol (SIP) first accoun | device,manager |
| GET | `/device/sip/settings` | Returns settings needed to configure calls with SIP first account.  Ac | device,manager |
| GET | `/device/sip2/enable` | Get information about Enabling/Disabling SIP second account | device,manager |
| POST | `/device/sip2/enable` | Turns On/Off calls with Session Initiation Protocol (SIP) second accou | device,manager |
| POST | `/device/sip2/settings` | Set second account SIP Settings | device,manager |
| GET | `/device/time` | Get current device time and timezone | status,manager |
| GET | `/device/uptime` | Returns the total time a device has been continuously powered on and r | status,admin |
| DELETE | `/forward/item/{forward-uid}` | Removes call forward rule for apartment | forward,manager |
| POST | `/forward/item/{forward-uid}` | - Create/Update forward rule. Forward incoming call from logic number  | forward,manager |
| DELETE | `/forward/items` | Delete multiple call forward rules | forward,manager |
| POST | `/forward/items/link` | Create/Update multiple call forward rules - This endpoint is used by L | forward,admin,link |
| POST | `/forward/mode` | Set call forward mode.  It can be used to call via P2P SIP or SIP for  | forward,manager |
| POST | `/keyproxy/mapping/version` | Configures key mapping type  This feature is available only in **BI**  | device,admin |
| GET | `/log/email/eventlist` | Returns the list of events which are used to trigger sending logs via  | log,manager |
| POST | `/log/email/eventlist` | Setup the list of events which will trigger sending log via mail. Ther | log,manager |
| POST | `/log/email/test` | Sends mail on saved recipient address using settings provided with `PO | log,manager |
| GET | `/log/photo/link` | Returns list of events which can be used to trigger sending photo from | log,admin |
| POST | `/log/photo/link` | Set list of events which can be used to trigger sending photo from cam | log,admin |
| POST | `/login` | Authenticate user credentials and return access token.  **Security Fea | auth |
| GET | `/login/change` | Returns whether the device is currently using the default password. If | auth |
| POST | `/login/change` | Setup new secure password.\nPassword Requirements:\nYour password must | auth |
| GET | `/logout` | Logs out the current session | auth |
| GET | `/network/mac` | Returns device MAC address | network,manager |
| DELETE | `/network/management/server/certificate` | Removes uploaded certificate for remote server settings with MQTT prot | network,manager,link |
| GET | `/network/management/server/debug` | Returns debug info when MQTT protocol is enabled  | network,manager,link |
| GET | `/network/settings` | Returns network settings. If DHCP option is enabled, response will con | network,manager |
| POST | `/network/settings/dhcp` | Turn on DHCP. Network will be automatically configured by DHCP server. | network,manager |
| POST | `/network/settings/static` | Set static network settings and turn off DHCP | network,manager |
| POST | `/network/timezone` | Set device timezone. NTP must be enabled. | network,manager |
| GET | `/network/timezone/manual` | Returns current timestamp, timezone and the list of supported timezone | network,admin |
| GET | `/security/banlist` | Returns list of banned IP addresses for login attempts with remaining  | auth,admin |
| PUT | `/security/banlist` | Add specified IP addresses to the login ban list.  It can be removed w | auth,admin |
| POST | `/security/password/manager` | Change manager password  | security,admin |
| DELETE | `/security/whitelist` | Clear the entire login whitelist, removing all IP addresses  | admin,auth |
| GET | `/security/whitelist` | Returns list of IP addresses whitelisted for login access  | admin,auth |
| POST | `/security/whitelist` | Remove specified IP addresses from the login whitelist  | admin,auth |
| PUT | `/security/whitelist` | Whitelist specified IP addresses for login access  | admin,auth |
| GET | `/syslog/clear` | Clear syslog - Device deletes logs older than six months automatically | log,admin |
| GET | `/syslog/file` | Returns zipped syslog - Device deletes logs older than six months auto | log,admin |
| GET | `/system/data/clear` | - Get array of available database tables to clear on device - Messages | system,manager |
| POST | `/system/data/clear` | **WARNING: This operation permanently deletes data and cannot be undon | system,manager |
| POST | `/system/debug/call/end` | Stop outgoing debug call | system |
| POST | `/system/debug/call/start` | Makes an outgoing call from device - Use this endpoint for call debug. | system |
| GET | `/system/debug/call/status` | Returns debug outgoing call status info | system |
| GET | `/system/debug/log` | Returns zip file with device system log for debugging | system,debug |
| GET | `/system/firmware/check/status` | Checks for firmware update on the server and returns info about latest | system,manager |
| POST | `/system/integrations/adc/disable` | Disables integration process with alarm.com. After disabling related c | admin,adc,system |
| GET | `/system/integrations/adc/status` | Returns status of integration: progress of firmware update, on what st | admin,adc,system |
| GET | `/system/reboot/run` | Reboot device | system,manager |
| POST | `/system/settings/backup/all` | Restore device settings from file | system,manager |
| POST | `/system/settings/default` | **WARNING: This operation is irreversible and will delete all user dat | system,admin |
| POST | `/system/settings/tables` | Restore users data from file | system,manager |
| GET | `/web/ssl` | Returns whether the local web server uses HTTPS | system,admin |
| GET | `/webhooks/events` | - Returns a list of Webhook Events with options could be used to sort  | admin,webhook,integration |
| GET | `/webhooks/events/retry/queue` | - Returns the list of Webhook Events marked as 'retrying' with options | admin,webhook,integration |
| POST | `/webhooks/events/{webhook-event-uid}/retry/now` | Sends webhook request immediately. Operation cannot be applied to even | admin,webhook,integration |
| DELETE | `/webhooks/{webhook-uid}` | - Removes Webhook Entity  | admin,webhook,integration |
| GET | `/webhooks/{webhook-uid}` | - Returns information about Webhook  | admin,webhook,integration |
| POST | `/webhooks/{webhook-uid}/test` | Sends test webhook request on provided URL.  | admin,webhook,integration |

## camdroid-lift-controller — current (33 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| POST | `/access/general/wiegand/type` | Adjusts the type of Wiegand used.  | access |
| POST | `/access/identifiers/link` | Delete multiple Identifier items by link_id param - This request is us | access,link |
| PUT | `/access/identifiers/link` | Create or Update multiple Identifier items. - This request is used by  | access,link |
| PATCH | `/access/identifiers/{uid}` | Update Identifier Entity - Available only in access control mode | access |
| POST | `/access/set/destination` | Activates controllers relays depends on floor/apartment entity binding | access |
| POST | `/device/address` | Set device logical address | device |
| GET | `/device/floor/map` | Get port mapping | device |
| POST | `/device/floor/map` | Set port mapping | device |
| POST | `/device/port/state` | Set port state - If the array is empty, it closes all ports | device |
| POST | `/device/settings` | Set device settings | device |
| GET | `/device/time` | Get device current time and timezone | status,device |
| GET | `/info` | Get information about:  - firmware version  - framework version  - fro | status |
| GET | `/log/items` | Get logs list. Available events: ### System * successful_login_api_cal | log |
| GET | `/login/change` | Returns whether the device is currently using the default password. If | auth |
| GET | `/logout` | Logout the current session | auth |
| GET | `/network/mac` | Returns device MAC address | network |
| GET | `/network/management/link` | Get Link server settings | network,link |
| GET | `/network/management/server` | Get management server settings.  If Link is enabled - server will sync | network,log,link |
| POST | `/network/management/server/certificate` | Uploads certificate (PEM format) for Link remote server settings with  | network,link |
| GET | `/network/management/server/debug` | Returns debug info when MQTT protocol is enabled  | network,link |
| GET | `/network/ntp` | Returns NTP Settings | network |
| POST | `/network/ntp` | Set NTP Settings | network |
| POST | `/network/settings/static` | Set network static settings and turn off dhcp | network |
| GET | `/network/timezone` | Get current timezone and available timezones list | network |
| POST | `/network/timezone` | Setup current timezone  | network |
| POST | `/security/password/admin` | Change web interface Admin password. Valid chars 0x20..0x7E | security |
| GET | `/system/firmware/check/status` | Returns info about latest firmware version on the server | system |
| POST | `/system/firmware/update/server` | Start firmware update from server or file. After successful start web  | system |
| POST | `/system/reboot/run` | Reboot device | system |
| GET | `/system/settings/backup/all` | Get backup file with device settings | system |
| POST | `/system/settings/backup/all` | Restore all the settings from backup | system |
| POST | `/system/settings/default` | Reset all settings to default | system |
| GET | `/system/settings/tables` | Get password-protected archive with users data: port mapping, identifi | system |

## camdroid-monitors — current (66 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| GET | `/advanced/dnd` | Get DND mode status, enabled or disabled | advanced |
| PUT | `/advanced/emergency` | Prepare preset with duration time and sound file for using during emer | advanced,emergency |
| POST | `/advanced/emergency/{entityUid}/start` | Start emergency playback by id | advanced,emergency |
| POST | `/advanced/emergency/{entityUid}/stop` | Start emergency playback by id | advanced,emergency |
| POST | `/advanced/forward` | Set forward numbers, up to 4 numbers | advanced |
| GET | `/advanced/ringtones` | Returns array of objects, where each object describes a ringtone | advanced |
| GET | `/advanced/ringtones/{ringtone-name}` | Downloads the ringtone file in .wav format | advanced |
| POST | `/advanced/standby/screen` | Standby mode represents splash screen when device is inactive. | advanced |
| GET | `/contacts` | Returns list of all contacts | contact |
| DELETE | `/contacts/{entityUid}` | Removes Contact Entity | contact |
| GET | `/contacts/{entityUid}` | Returns Contact Entity detailed information. | contact |
| PUT | `/contacts/{entityUid}` | You can update contact with the next types: - `regular` - for monitors | contact |
| GET | `/device/call/auto_hangup` | Returns hangup settings  | device |
| GET | `/device/call/concierge` | Get external concierge number and feature status. If enabled - device  | device |
| POST | `/device/call/concierge` | Set external concierge number and feature status. If enabled - device  | device |
| GET | `/device/call/fixed-numbers` | Get a list of fixed dialer numbers. - this feature is only available o | device |
| POST | `/device/call/fixed-numbers` | Set a list of fixed dialer numbers. - this feature is only available o | device |
| GET | `/device/intercom/apartment` | Returns logical address info. Logical address - entity used as a call  | device |
| POST | `/device/intercom/apartment` | Set logical address info. Logical address - entity used as a call numb | device |
| POST | `/device/multicast/paging` | set multicast settings | device |
| GET | `/device/settings/dtmf/codes` | Get DTMF code setting for first and second locks | device |
| POST | `/device/settings/dtmf/codes` | Set DTMF code setting for first and second locks | device |
| GET | `/device/settings/light_indication` | Get the settings of the incoming call and the doorbell external light  | device |
| POST | `/device/settings/light_indication` | Set the settings of the incoming call and the doorbell external light  | device |
| POST | `/device/settings/volume` | Set talk, incoming call and buttons press volume levels | device |
| GET | `/device/sip/enable` | Check if SIP enabled or not | device |
| GET | `/device/sip/reregister` | Get SIP auto reregister settings | device |
| POST | `/device/sip/reregister` | Set SIP auto reregister every N seconds if registration is interrupted | device |
| GET | `/device/sip/settings` | Get device SIP settings  | device |
| GET | `/device/time` | Get device current time and timezone | status |
| POST | `/link/announcement` | Send announcement to device from Link or other server. Announcement wi | link,announcement |
| POST | `/link/contacts` | Removes Contacts by theirs uids  | contact,link |
| PUT | `/link/contacts` | Creates or updates contacts  | contact,link |
| GET | `/login` | Collect a Bearer token for a registered user. Token lifetime - 2 hours | auth |
| GET | `/network/mac` | Returns Ethernet adapter MAC address | network |
| GET | `/network/management/link` | Get Link server settings | network |
| POST | `/network/management/link` | Set Link server settings | network |
| GET | `/network/management/server` | Get management server settings.  If Link is enabled - server will sync | network,log,link |
| POST | `/network/management/server` | Set management server settings.  If Link is enabled - Link will sync i | network,log,link |
| DELETE | `/network/management/server/certificate` | Removes uploaded certificate for Link remote server settings with MQTT | network,link |
| GET | `/network/management/server/certificate` | Returns info about using SSL certificate for Link remote server MQTT p | network,link |
| GET | `/network/management/server/debug` | Returns debug info when MQTT protocol is enabled  | network,link |
| GET | `/network/ntp` | Returns NTP Settings | network |
| POST | `/network/ntp` | Set Ntp Settings | network |
| GET | `/network/settings` | Returns Ethernet network settings. If DHCP option is enabled, response | network |
| POST | `/network/settings/static` | Set Ethernet network static settings and turn off dhcp | network |
| POST | `/network/timezone` | Setup current timezone  | network |
| GET | `/security/ipcam` | Get connected IP cameras list and their settings | security,ipcam |
| POST | `/security/monitors/sos` | Change SOS-monitors list or add new one | security |
| POST | `/security/password/web/admin` | Change web interface Admin password. - Valid characters with codes fro | security,admin |
| GET | `/security/scene` | Get security scene status and scenes list | security |
| POST | `/security/scene` | Set security scene. Available only on the master device | security |
| GET | `/security/scene/settings` | Return all the scenes activation settings | security |
| GET | `/security/zone` | Get information about security zones | security |
| POST | `/security/zone` | Set security zones settings. Available only on the master device. | security |
| GET | `/sip/status` | Get current SIP registration status  | status |
| POST | `/system/call/photo` | Enable/disable saving of the made on call photo to logs | system |
| GET | `/system/firmware/check/status` | Returns info about latest firmware version on the server | system |
| GET | `/system/firmware/server/custom` | Get custom updates server address. Server used in projects with custom | system |
| POST | `/system/firmware/update/server` | Start firmware update from server or file. After successful start web  | system |
| POST | `/system/settings/backup/all` | Restore all the settings from backup | system |
| POST | `/system/support/service` | Enable/disable "remote connection" feature | system |
| GET | `/wifi/connection` | Get information about the current Wi-Fi connection | network |
| GET | `/wifi/mode` | Get Wi-Fi mode | network |
| POST | `/wifi/mode` | Set Wi-Fi mode | network |
| GET | `/wifi/settings` | Returns Wi-Fi settings. If DHCP option is enabled, response will conta | network |

## camdroid-panels — current (145 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| GET | `/access/door/sensor` | Returns info about door sensor options | access |
| POST | `/access/door/sensor` | Customize door sensor feature. There are 2 available modes: - door_sen | access |
| POST | `/access/exit/button/toggle` | Set status of the exit button contacts feature. If disabled, the door  | access |
| DELETE | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| GET | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| POST | `/access/general/elevator/floor` | This endpoint is deprecated, use `POST /access/general/elevator/settin | access,admin |
| GET | `/access/general/elevator/settings` | Returns panel floor number and lift call actions status.  The function | access,admin |
| POST | `/access/general/elevator/settings` | Configures panel floor number and lift call actions.  The function wor | access,admin |
| POST | `/access/general/lock/close/emergency` | Cancel emergency mode and close the locks | access,admin |
| GET | `/access/general/lock/delay/{lockNumber}` | Time delay before panel relay contacts will be open | access,admin |
| GET | `/access/general/lock/dtmf/{lockNumber}` | Get DTMF codes for door locks - Not available on CR-02BD | access |
| POST | `/access/general/lock/dtmf/{lockNumber}` | Set DTMF codes for door locks - Not available on CR-02BD | access |
| GET | `/access/general/lock/ext_locks` | Get external locks settings | access |
| GET | `/access/general/lock/open/remote/accepted/{lockNumber}` | Open lock and trigger "access allowed" event via HTTP. In logs will be | access,admin |
| GET | `/access/general/lock/open/remote/control/denied` | Show on display/play sound "access denied" via HTTP (for Remote Access | access,admin |
| GET | `/access/general/lock/timeout/{lockNumber}` | Time for which the relay contacts will be closed after opening | access,admin |
| POST | `/access/general/lock/timeout/{lockNumber}` | Time for which the relay contacts will be closed after opening | access,admin |
| POST | `/access/general/lock/type` | Set the type of lock used:   - electromagnetic   - electromechanical | access,admin |
| POST | `/access/general/unlock/card/master` | Set master card number. - Master card can be used to add another cards | access,admin |
| GET | `/access/general/unlock/input/code` | Get master access code and feature status. Available only on panels wi | access,admin |
| POST | `/access/general/wiegand` | Configures Wiegand input/output.  Wiegand type. All data received on W | access,admin |
| GET | `/access/general/wiegand/type` | Gets the type of Wiegand used.  | access,admin |
| POST | `/access/general/wiegand/type` | Adjusts the type of Wiegand used.  | access,admin |
| POST | `/access/identifier` | Create Identifier Entity. You can create identifiers with the next typ | access,admin |
| POST | `/access/identifier/item/{identifier-uid}/timeprofile/{timeprofile-uid}` | Attach time profile to identifier | access,admin |
| DELETE | `/access/identifier/item/{identifierUid}` | Delete Identifier Entity | access,admin |
| PATCH | `/access/identifier/item/{identifierUid}` | Update Identifier Entity | access,admin |
| GET | `/access/identifier/item/{identifierUid}/qr` | Returns png representation of the stored QR identifier | access,admin |
| GET | `/access/identifier/items` | Returns identifiers list with options could be used to sort and filter | access,admin |
| DELETE | `/access/identifier/items/link` | Delete multiple Identifier items by `link_id` param. This request is u | access,link,admin |
| GET | `/access/identifier/items/link` | Get multiple Identifier items with `link_id`.  This can be used by 3d- | access,link,admin |
| POST | `/access/locks/settings` | Set the settings for all locks - Not available on CR-02BD - The DTMF v | access |
| POST | `/access/timeprofile` | Create Time Profile Entity. It describes access rules which can be att | access,admin |
| GET | `/access/timeprofile/item/{timeProfileUid}` | Returns Time Profile Entity | access,admin |
| GET | `/access/timeprofile/items` | Returns Time Profiles list | access,admin |
| DELETE | `/access/timeprofile/items/link` | Delete multiple Time Profile items by `link_id` param. This request is | access,link,admin |
| GET | `/access/timeprofile/items/link` | Get multiple Time Profile items with `link_id`.  This can be used by 3 | access,link,admin |
| POST | `/access/timeprofile/items/link` | Create or Update multiple Time Profile items.  This request is used by | access,admin,link |
| POST | `/advanced/notification/call-start` | Enable/Disable start call sound feature | advanced |
| GET | `/advanced/notification/call-start/sound` | Returns custom start call sound settings | advanced |
| PATCH | `/advanced/notification/call-start/sound` | Uploads custom start call sound file | advanced |
| POST | `/advanced/notification/conversation-start` | Enable/Disable conversation start sound feature | advanced |
| DELETE | `/advanced/notification/conversation-start/sound` | Removes custom conversation start sound | advanced |
| GET | `/advanced/notification/conversation-start/sound` | Returns custom conversation start sound settings | advanced |
| DELETE | `/advanced/notification/incoming-call/sound` | Removes custom incoming call ringtone sound. Device will use default s | advanced |
| PATCH | `/advanced/notification/incoming-call/sound` | Uploads custom incoming call ringtone sound file | advanced |
| POST | `/advanced/notification/incoming-call/sound` | Enable/Disable custom incoming call ringtone feature | advanced |
| GET | `/advanced/notification/ringing/tone/sound` | Returns custom ringing tone settings | advanced |
| POST | `/advanced/notification/ringing/tone/sound` | Enable/Disable custom ringing tone feature | advanced |
| GET | `/advanced/notification/sound/file` | Downloads any uploaded custom sound | advanced |
| GET | `/advanced/rtsp/feed` | The function of viewing additional IP cameras during a call (up to 4 s | advanced |
| POST | `/advanced/rtsp/feed` | The function of viewing additional IP cameras during a call (up to 4 s | advanced |
| POST | `/apartment` | Creates Apartment Entity. The `uid` value returned in the response can | apartment |
| GET | `/apartment/item/{apartmentUid}` | Returns Apartment Entity detailed information.  Base Apartment Entity  | apartment,admin |
| GET | `/apartment/items` | Return Apartments entities detailed list with used pagination, filter, | apartment,admin |
| GET | `/apartment/items/link` | Get multiple Apartment Entities with `link_id`. | apartment,link,admin |
| POST | `/desktop/settings/access` | Set a password for GUI settings access - This feature is available onl | admin,security |
| POST | `/desktop/settings/access/enable` | Set GUI settings access | admin,security |
| GET | `/device/call/auto_answer` | Get auto answer feature status | device |
| POST | `/device/call/concierge` | Configure concierge number settings. * If enabled panel will call to p | device |
| GET | `/device/call/dial/auto` | The function of automatic dialing after entering the number digits spe | device |
| POST | `/device/call/dial/auto` | The function of automatic dialing after entering the number digits spe | device,multiapartment |
| GET | `/device/call/dial/timeout` | Returns time interval after which the panel automatically ends an outg | device |
| GET | `/device/call/drop/lock-open` | Returns the call termination options when the lock is opened | device |
| POST | `/device/call/drop/lock-open` | Sets the call termination options when the lock is opened | device |
| GET | `/device/call/talk/timeout` | Returns the time interval after which the panel automatically ends the | device |
| GET | `/device/camera/light_settings` | Gets the settings for turning on the backlight and switching to the BW | camera |
| POST | `/device/camera/light_settings` | Posts the settings for turning on the backlight and switching to the B | camera |
| GET | `/device/camera/mode` | Provides info about current camera mode: - qr_reader (with RTSP) - rts | camera |
| POST | `/device/camera/mode` | Setup camera mode: - qr_reader (with RTSP) - rtsp_server | camera |
| GET | `/device/control4/settings` | Get the settings for integration with `Control4`. - Not available on C | integration,control4 |
| GET | `/device/feature/dispatch-service` | Get the settings for dispatch service mode. - this feature is only ava | feature,device |
| POST | `/device/feature/dispatch-service` | Set the settings for rescuer service mode. - this feature is only avai | feature,device |
| GET | `/device/feature/help-station` | Get help station settings  - This feature is only available on idividu | feature,device |
| POST | `/device/feature/help-station` | Customize help station feature. - This feature is only available on id | feature,device |
| GET | `/device/feature/rescue-service` | Get the settings for rescuer service mode. - this feature is only avai | feature,device |
| POST | `/device/feature/rescue-service` | Set the settings for rescuer service mode. - This feature is only avai | feature,device |
| GET | `/device/language` | Get current system language and the list of supported languages | status |
| POST | `/device/language` | Set current system language | status |
| GET | `/device/mode/current` | Returns current panel work mode | device |
| POST | `/device/mode/unit` | Set panel work mode to `Unit` mode.  In `Unit` mode you must enter flo | device |
| POST | `/device/mode/wall` | Set panel work mode to `Wall` mode. - In `Wall` mode you must enter fu | device |
| GET | `/device/relay/settings` | Get relay boot position | device |
| GET | `/device/security/tamper` | - Returns current tamper settings    - This option is available on the | security,system |
| POST | `/device/security/tamper` | - Turns on/off tamper - This option is available on the following devi | security,system |
| GET | `/device/settings/payload` | Returns information about video Real-time Transport Protocol (RTP) pro | device |
| POST | `/device/settings/payload` | Configure video Real-time Transport Protocol (RTP) profile. It specifi | device |
| GET | `/device/settings/rtsp` | Returns **username** used to access panel's camera RTSP stream - Camer | device |
| POST | `/device/settings/rtsp` | Set **username** and **password** used to access panel's camera RTSP s | device |
| GET | `/device/settings/video` | Returns camera video resolution - Available resolution for panels with | device |
| POST | `/device/settings/video` | Set video resolution - Available resolution for panels with **1-megapi | device |
| POST | `/device/settings/volume` | Set speaker volume level | device |
| GET | `/device/sip/enable` | Get information about Enabling/Disabling SIP | device |
| POST | `/device/sip/enable` | Turns On/Off calls with Session Initiation Protocol (SIP) | device |
| GET | `/device/sip/regfailunlock` | Get feature status and timer before relay unlock if SIP registration f | access,admin |
| POST | `/device/sip/regfailunlock` | Set feature status and timer before relay unlock if SIP registration f | access,admin |
| GET | `/device/sip/settings` | Returns settings needed to configure calls with SIP | device |
| GET | `/device/uptime` | Returns the total time a device has been continuously powered on and r | status,admin |
| DELETE | `/forward/item/{forwardUid}` | Removes call forward rule for apartment | forward |
| POST | `/forward/item/{forwardUid}` | Create/Update call forward rule | forward |
| DELETE | `/forward/items` | Delete multiple call forward rules | forward |
| GET | `/forward/items` | Returns call forward rules sorted list with pagiantion options | forward |
| GET | `/forward/items/link` | Get multiple call forward rules with link_id | forward,link |
| POST | `/forward/items/link` | Create/Update multiple call forward rules with link_id - This endpoint | forward,link |
| GET | `/forward/mode` | Get call forward mode.  It can be used to call via P2P SIP or SIP for  | forward |
| GET | `/log/items` | Get logs list. Available events:  ### Access * access_denied_by_not_va | log |
| GET | `/log/photo/link` | Returns list of events which can be used to trigger sending photo from | log,admin |
| POST | `/login/change` | Setup new secure password.\nPassword Requirements:\nYour password must | auth |
| GET | `/network/debug/capture` | Returns network capture data | network |
| POST | `/network/debug/capture/start` | Start the capturing network packets | network |
| GET | `/network/debug/capture/status` | Get network capture status | network |
| GET | `/network/dst` | Returns Daylight Saving Time (DST) settings.  DST is a seasonal time c | network |
| POST | `/network/dst` | Configures DST settings.  DST is a seasonal time change measure where  | network |
| GET | `/network/management/link` | Get management server settings.  If Link is enabled - Link will sync i | link,log,network |
| POST | `/network/management/link` | Set management server settings.  If Link is enabled - Link will sync i | log,network,link |
| GET | `/network/management/server` | Get management server settings.  If Link is enabled - server will sync | network,link |
| DELETE | `/network/management/server/certificate` | Removes uploaded certificate for Link remote server settings with MQTT | network,link |
| GET | `/network/management/server/certificate` | Returns info about using certificate for Link remote server MQTT proto | network,link |
| POST | `/network/management/server/certificate` | Uploades certificate (PEM format) for Link remote server settings with | network,link |
| GET | `/network/ntp` | Get NTP server address | network |
| POST | `/network/ntp` | Set NTP server address | network |
| GET | `/network/settings` | Returns network settings. If DHCP option is enabled, response will con | network |
| POST | `/network/settings/dhcp` | Turn on DHCP. Network will be automatically configured by DHCP server. | network |
| POST | `/network/settings/static` | Set static network settings and turn off DHCP | network |
| GET | `/network/timezone` | Get current timezone and list of available timezones | network |
| POST | `/network/timezone` | Set device timezone. NTP server address must be set. | network |
| DELETE | `/security/banlist` | Removes all IP addresses from the ban list and unbans them - Available | security |
| GET | `/security/banlist` | Returns the list of banned IPs - Available on all panels | security |
| POST | `/security/password/web/admin` | Change web interface Admin password. Valid chars 0x20..0x7E | security,admin |
| DELETE | `/security/whitelist` | Removes all IP addresses from the white list - Available on all panels | security |
| POST | `/security/whitelist` | Deletes the IP addresses from the white list - Available on all panels | security |
| PUT | `/security/whitelist` | Adds the IP addresses from the white list - Available on all panels | security |
| GET | `/sip/status` | Get current SIP registration status. Awailable statuses:   * `OK` - de | status |
| GET | `/system/analytics` | Describes whether analytics collection is enabled on the device.  Rest | system |
| POST | `/system/analytics` | Enable/disable analytics collection on the device. Enabled (`is_enable | system |
| POST | `/system/data/clear` | Removes table data, such as identifiers, apartments, access rules, for | system |
| GET | `/system/firmware/check/status` | Checks for firmware update on the server and returns info about latest | system |
| POST | `/system/firmware/update/file` | Upload firmware image and start update | system |
| GET | `/system/reboot/run` | Reboot device | system |
| GET | `/system/settings/backup/all` | Get password-protected archive with device settings.  Backup does not  | system |
| POST | `/system/settings/backup/all` | Restore device settings from file | system |
| POST | `/system/settings/default` | - Reset device to factory settings - Removes all user data: identifier | system |
| POST | `/system/settings/tables` | Restore users data from file | system |
| GET | `/system/support/service` | Describes feature status, support team will be allowed to connect if v | system |
| POST | `/system/support/service` | Enable/disable "remote connection" feature | system |

## door-controller — current (78 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| GET | `/access/access-rules` | Returns Access rules list | access,access rules |
| POST | `/access/access-rules/link/delete` | Delete multiple Access rule items by `link_id` param. This request is  | access,link,access rules |
| DELETE | `/access/access-rules/{access-rule-id}` | Delete Access rule Entity | access,access rules |
| POST | `/access/access-rules/{access-rule-id}/time-profiles/{time-profile-id}` | Attach Time Profile rule to Access Rule | access,access rules,time profiles |
| GET | `/access/general/lock-room` | If one of door sensors opened or one of exit buttons long pressed - an | access |
| GET | `/access/general/unlock/card/master` | Get master card number. Master card can be used to add another cards t | access |
| POST | `/access/general/unlock/card/master` | Set master card number. - Master card can be used to add another cards | access |
| GET | `/access/identifiers` | Returns identifiers list with options could be used to sort and filter | access,identifiers |
| POST | `/access/identifiers/delete` | Delete multiple Identifier items | access,identifiers |
| POST | `/access/identifiers/link` | Create or Update multiple Identifier items.  This request is used by ` | access,link,identifiers |
| POST | `/access/identifiers/outdated/autoremove` | Set current state of clearing outdated identifiers. After 7 days after | access,identifiers |
| DELETE | `/access/identifiers/{identifier-id}` | Delete Identifier Entity | access,identifiers |
| GET | `/access/identifiers/{identifier-id}` | Returns detailed info about Identifier | access,identifiers |
| PATCH | `/access/identifiers/{identifier-id}` | Update Identifier Entity | access,identifiers |
| POST | `/access/identifiers/{identifier-id}/passes/reset` | Reset left passes to max, if there is a restriction on the number of p | access,identifiers |
| POST | `/access/plate/check` | Allows to send data from camera to device, so device will be able to p | device |
| GET | `/access/time-profiles/{time-profile-id}` | Returns Time Profile Entity | access,time profiles |
| GET | `/access/users` | Returns users list with options could be used to sort and filter them  | access,users |
| PUT | `/access/users` | Creates user entity  | access,users |
| POST | `/access/users/delete` | Allows making massive user deletion by their unique ids | access,users |
| DELETE | `/access/users/identifiers/{identifier-id}` | Allows to detach identifier from user | access,users,identifiers |
| POST | `/access/users/link` | Create/update multiple User Entities with `link_id`.  If entity doesn' | access,link,users |
| POST | `/access/users/link/delete` | Delete multiple User Entities with `link_id`. If user with provided `l | access,link,users |
| DELETE | `/access/users/{user-id}` | Deletes User Entity | access,users |
| GET | `/access/users/{user-id}` | Returns detailed info about User | access,users |
| PATCH | `/access/users/{user-id}` | Updates User Entity `has_duplicates` - if user with the same name alre | access,users |
| DELETE | `/access/users/{user-id}/access-rules/{access-rule-id}` | Detach Access rule from User | access,users |
| POST | `/access/users/{user-id}/access-rules/{access-rule-id}` | Attach Access rule to user | access,users,access rules |
| GET | `/access/users/{user-id}/apartments` | Return the list of attached apartments | users,access |
| GET | `/access/users/{user-id}/time-profiles` | Return the list of time profiles | users,access |
| DELETE | `/access/users/{user-id}/time-profiles/{time-profile-id}` | Allows to detach time profile from user | access,users,time profiles |
| PUT | `/apartments` | Creates Apartment Entity. The `id` value returned in the response can  | apartments |
| POST | `/apartments/delete` | Delete multiple apartment items by their unique ids | apartments |
| POST | `/apartments/link` | Create/update multiple Apartment Entities with `link_id`.  If entity d | apartments,link |
| PATCH | `/apartments/{apartment-id}` | Update Apartment Entity base information | apartments |
| GET | `/apartments/{apartment-id}/identifiers` | Return the list of attached identifiers | apartments |
| POST | `/apartments/{apartment-id}/users/{user-id}` | Allows to add user to apartment | apartments,users |
| GET | `/device/interfaces/controlled-inputs` | Returns settings for controlled inputs that can be used to close one o | device |
| POST | `/device/interfaces/controlled-inputs` | Set settings for controlled inputs that can be used to close one or mo | device |
| POST | `/device/interfaces/door-sensors` | Set door sensors settings | device |
| GET | `/device/interfaces/fire-alarm/settings` | Returns fire alarm input interface settings | device |
| POST | `/device/interfaces/fire-alarm/status` | Apply fire alarm input interface new status | device |
| GET | `/device/interfaces/osdp/debug` | Get OSDP debug info | device |
| GET | `/device/interfaces/osdp/devices` | Returns list of OSDP devices notification settings | device |
| PUT | `/device/interfaces/osdp/devices` | Create new OSDP device notification settings | device |
| POST | `/device/interfaces/osdp/devices/{rs485-number}/{osdp-device-address}/configure` | Configure OSDP device parameters | device |
| GET | `/device/interfaces/osdp/devices/{rs485-number}/{osdp-device-address}/ping` | Tries to connect to OSDP device and get its information | device |
| GET | `/device/interfaces/rs485` | Returns RS-485 serial bus settings | device |
| POST | `/device/interfaces/rs485` | Set RS-485 serial bus settings | device |
| GET | `/device/interfaces/security-alarm/status` | Returns security alarm input interface current status | device |
| GET | `/device/interfaces/wiegand-inputs` | Returns settings for wiegand inputs that can be used to read identifie | device |
| GET | `/device/led/settings` | Returns LED settings | device |
| GET | `/device/readers` | Describes list of readers available, readers can be used in access-rul | access |
| POST | `/device/relays/open/{relay-number}` | Open relay and trigger "access allowed" event via HTTP. In logs will b | access |
| GET | `/device/relays/settings` | Returns general settings for all device relays.  | access |
| POST | `/device/relays/settings` | Setup device relays settings  | access |
| POST | `/device/security/tamper` | - Turns on/off tamper feature | security,system |
| POST | `/device/time` | Sets the date, time and timezone on the device, configure Ntp settings | device |
| GET | `/info` | Get information about:  - firmware version  - API version  - device mo | status |
| GET | `/logs` | Return log's list. Available events: | log |
| GET | `/network/mac` | Returns device MAC address | network |
| GET | `/network/mac/wifi` | Returns device Wi-Fi MAC address | network |
| GET | `/network/management/server` | Get management server settings.  If Link is enabled - server will sync | network,log,link |
| POST | `/network/management/server` | Set management server settings.  If Link is enabled - Link will sync i | network,log,link |
| GET | `/network/management/server/certificate` | Returns info about using certificate for remote server MQTT protocol | network,link |
| POST | `/network/management/server/certificate` | Uploads certificate for remote server settings with MQTT protocol.  | network,link |
| GET | `/network/management/server/debug` | Returns debug info when MQTT protocol is enabled  | network,link |
| GET | `/network/settings/wifi` | Returns Wi-Fi network settings. If DHCP option is enabled, response wi | network |
| POST | `/network/settings/wifi` | Set Wi-Fi network settings. If DHCP option is enabled, other parameter | network |
| POST | `/network/settings/wifi/connection` | Set Wi-Fi interface connection parameters | network |
| POST | `/network/settings/wifi/mode` | Set Wi-Fi interface mode | network |
| POST | `/security/password/admin` | Change admin password | security |
| GET | `/system/data/clear` | - Getting array of available database tables to clear on device | system |
| GET | `/system/data/export` | Get archive with users data: identifiers, apartments, time profiles, a | system |
| POST | `/system/data/import` | Restore users data from file | system |
| GET | `/system/firmware/check/status` | Checks for firmware update on the server and returns info about latest | system |
| GET | `/system/firmware/server/custom` | Get custom firmware updates server settings.  Can be used if the user  | system |
| POST | `/system/firmware/server/custom` | Get custom firmware updates server settings. Can be used if the user h | system |

## ingenic-mips-panels — current (142 операций)

| Метод | Путь | Название | Теги |
|---|---|---|---|
| POST | `/access/door/sensor` | Customize door sensor feature. There are 2 available modes: - door_sen | access |
| GET | `/access/exit/button/toggle` | Returns status of the exit buttons contacts feature. If disabled, the  | access |
| POST | `/access/exit/button/toggle` | Set status of the exit button contacts feature. If disabled, the door  | access |
| GET | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| POST | `/access/general/elevator/devices` | PLEASE BE NOTED THAT THIS FEATURE WORKS ONLY WITH EVRC-IP VERSION 2.2. | access,admin |
| GET | `/access/general/elevator/floor` | This endpoint is deprecated, use `GET /access/general/elevator/setting | access,admin |
| POST | `/access/general/elevator/floor` | This endpoint is deprecated, use `POST /access/general/elevator/settin | access,admin |
| POST | `/access/general/elevator/settings` | Configures panel floor number and lift call actions.  The function wor | access,admin |
| GET | `/access/general/lock/delay/{lockNumber}` | Time delay before panel relay contacts will be open | access,admin |
| GET | `/access/general/lock/dtmf/{lockNumber}` | Get DTMF codes for door locks | access |
| GET | `/access/general/lock/ext_locks` | Get external locks settings - Not available on AV-06 | access |
| POST | `/access/general/lock/open/emergency` | 'Open the locks in emergency mode for the specified time, unlock time  | access,admin |
| GET | `/access/general/lock/open/remote/control/accepted/{lockNumber}` | Open lock and trigger "access allowed" event via HTTP (for Remote Acce | access,admin |
| GET | `/access/general/lock/timeout/{lockNumber}` | Time for which the relay contacts will be closed after opening | access,admin |
| POST | `/access/general/lock/timeout/{lockNumber}` | Time for which the relay contacts will be closed after opening | access,admin |
| GET | `/access/general/lock/type` | Gets the type of lock used:   - electromagnetic   - electromechanical | access,admin |
| POST | `/access/general/lock/type` | Set the type of lock used:   - electromagnetic   - electromechanical | access,admin |
| GET | `/access/general/remote/control/settings` | Get remote access server settings. \n\nIf enabled - panel sends reques | access |
| GET | `/access/general/security/monitor` | 'If the feature is enabled, then when the card brought to the reader t | access,admin |
| POST | `/access/general/security/monitor` | 'If the feature is enabled, then when the card brought to the reader t | access,admin |
| GET | `/access/general/unlock/card/master` | Get master card number. - Master card can be used to add another cards | access,admin |
| POST | `/access/general/unlock/input/code` | Set master access code and feature status. Available only on panels wi | access,admin |
| GET | `/access/general/wiegand` | Returns Wiegand input and output settings.  Wiegand type. All data rec | access,admin |
| POST | `/access/general/wiegand` | Configures Wiegand input/output.  Wiegand type. All data received on W | access,admin |
| GET | `/access/general/wiegand/type` | Gets the type of Wiegand used. - Not available on AV-06  | access,admin |
| POST | `/access/general/wiegand/type` | Adjusts the type of Wiegand used. - Not available on AV-06  | access,admin |
| DELETE | `/access/identifier/item/{identifier-uid}/timeprofile/{timeprofile-uid}` | Detach time profile from identifier | access,admin |
| DELETE | `/access/identifier/item/{identifierUid}` | Delete Identifier Entity | access,admin |
| GET | `/access/identifier/item/{identifierUid}/qr` | Returns png representation of the stored QR identifier | access,admin |
| GET | `/access/identifier/items` | Returns identifiers list with options could be used to sort and filter | access,admin |
| DELETE | `/access/identifier/items/link` | Delete multiple Identifier items by `link_id` param. This request is u | access,link,admin |
| GET | `/access/identifier/items/link` | Get multiple Identifier items with `link_id`.  This can be used by 3d- | access,link,admin |
| POST | `/access/identifier/items/link` | Create or Update multiple Identifier items.  This request is used by ` | access,admin,link |
| POST | `/access/locks/settings` | Set the settings for all locks - The DTMF value for elevator calling a | access |
| POST | `/access/plate/check` | 'Allows to send data from camera to device, so device will be able to  | access |
| POST | `/access/timeprofile` | Create Time Profile Entity. It describes access rules which can be att | access,admin |
| DELETE | `/access/timeprofile/item/{timeProfileUid}` | Delete Time Profile Entity | access,admin |
| GET | `/access/timeprofile/item/{timeProfileUid}` | Returns Time Profile Entity | access,admin |
| PATCH | `/access/timeprofile/item/{timeProfileUid}` | Update Time Profile Entity | access,admin |
| GET | `/access/timeprofile/items` | Returns Time Profiles list | access,admin |
| GET | `/access/timeprofile/items/link` | Get multiple Time Profile items with `link_id`.  This can be used by 3 | access,link,admin |
| POST | `/access/timeprofile/items/link` | Create or Update multiple Time Profile items.  This request is used by | access,admin,link |
| POST | `/advanced/notification/call-start` | Enable/Disable start call sound feature | advanced |
| DELETE | `/advanced/notification/call-start/sound` | Removes custom start call sound | advanced |
| PATCH | `/advanced/notification/call-start/sound` | Uploads custom start call sound file | advanced |
| POST | `/advanced/notification/call-start/sound` | Enable/Disable custom start call sound feature | advanced |
| GET | `/advanced/notification/conversation-start` | Returns conversation start sound state information | advanced |
| POST | `/advanced/notification/conversation-start` | Enable/Disable conversation start sound feature | advanced |
| GET | `/advanced/notification/conversation-start/sound` | Returns custom conversation start sound settings | advanced |
| DELETE | `/advanced/notification/incoming-call/sound` | Removes custom incoming call ringtone sound. Device will use default s | advanced |
| PATCH | `/advanced/notification/incoming-call/sound` | Uploads custom incoming call ringtone sound file | advanced |
| POST | `/advanced/notification/incoming-call/sound` | Enable/Disable custom incoming call ringtone feature | advanced |
| PATCH | `/advanced/notification/lock/open/sound` | Uploads custom lock open sound file | advanced |
| POST | `/advanced/notification/lock/open/sound` | Enable/Disable custom lock open sound feature | advanced |
| PATCH | `/advanced/notification/ringing/tone/sound` | Uploads custom ringing tone sound file | advanced |
| POST | `/advanced/notification/ringing/tone/sound` | Enable/Disable custom ringing tone feature | advanced |
| POST | `/advanced/rtsp/feed` | The function of viewing additional IP cameras during a call (up to 4 s | advanced |
| POST | `/apartment` | Creates Apartment Entity. The `uid` value returned in the response can | apartment |
| DELETE | `/apartment/item/unbind/identifier/{identifierUid}` | Delete a relation between the identifier and the apartment entities | apartment,admin |
| GET | `/apartment/item/{apartmentUid}` | Returns Apartment Entity detailed information.  Base Apartment Entity  | apartment,admin |
| GET | `/apartment/items` | 'Return Apartments entities detailed list with used pagination, filter | apartment,admin |
| DELETE | `/apartment/items/link` | Delete multiple Apartment Entities with `link_id`.  If apartment with  | apartment,admin,link |
| POST | `/apartment/items/link` | Create/update multiple Apartment Entities with `link_id`.  If entity d | apartment,admin,link |
| GET | `/device/call/auto_answer` | Get auto answer feature status | device |
| POST | `/device/call/auto_answer` | Turn on/off auto answer | device |
| GET | `/device/call/concierge` | Configure concierge number settings. * If enabled panel will call to p | device |
| GET | `/device/call/drop` | Get end the call by pressing call button feature status. Available onl | device,individual |
| POST | `/device/call/drop` | Set end the call by pressing call button feature status. Available onl | device |
| GET | `/device/call/drop/lock-open` | Returns the call termination options when the lock is opened | device |
| GET | `/device/call/talk/timeout` | Returns the time interval after which the panel automatically ends the | device |
| GET | `/device/camera/mode` | Provides info about current camera mode: - qr_reader (with RTSP) - rts | camera |
| GET | `/device/feature/dispatch-service` | Get the settings for dispatch service mode. - this feature is only ava | feature,device |
| POST | `/device/feature/dispatch-service` | Set the settings for rescuer service mode. - this feature is only avai | feature,device |
| GET | `/device/feature/help-station` | Get help station settings  - This feature is only available on idividu | feature,device |
| GET | `/device/feature/rescue-service` | Get the settings for rescuer service mode. - this feature is only avai | feature,device |
| POST | `/device/feature/rescue-service` | Set the settings for rescuer service mode. - This feature is only avai | feature,device |
| POST | `/device/language` | Set current system language | status |
| POST | `/device/mode/apartment` | Set Panel work mode to `Apartment` mode | device |
| GET | `/device/mode/current` | Returns current panel work mode | device |
| POST | `/device/mode/unit` | Set panel work mode to `Unit` mode.  In `Unit` mode you must enter flo | device |
| POST | `/device/mode/wall` | Set panel work mode to `Wall` mode. - In `Wall` mode you must enter fu | device |
| POST | `/device/relay/settings` | Set relay boot position | device |
| GET | `/device/sdcard/info` | Get the sd card information - Not available on AV-06 | device |
| POST | `/device/security/tamper` | - Turns on/off tamper - This option is available on the following devi | security,system |
| POST | `/device/settings/payload` | Configure video Real-time Transport Protocol (RTP) profile. It specifi | device |
| GET | `/device/settings/video` | Returns camera video resolution - Available resolution for panels with | device |
| POST | `/device/settings/volume` | Set speaker volume level | device |
| POST | `/device/sip/enable` | Turns On/Off calls with Session Initiation Protocol (SIP) | device |
| POST | `/device/sip/regfailunlock` | Set feature status and timer before relay unlock if SIP registration f | access,admin |
| POST | `/device/sip/reregister` | Set SIP auto reregister every N seconds. If there is no request body,  | device,admin |
| GET | `/device/time` | Get current device time and timezone | status,device |
| DELETE | `/forward/item/{forwardUid}` | Removes call forward rule for apartment | forward |
| POST | `/forward/item/{forwardUid}` | Create/Update call forward rule | forward |
| DELETE | `/forward/items` | Delete multiple call forward rules | forward |
| GET | `/forward/items` | Returns call forward rules sorted list with pagiantion options | forward |
| POST | `/forward/items/link` | Create/Update multiple call forward rules with link_id - This endpoint | forward,link |
| POST | `/forward/mode` | Set call forward mode.  It can be used to call via P2P SIP or SIP for  | forward |
| GET | `/login` | Used to collect a Bearer token for a registered user | auth |
| GET | `/login/change` | Returns whether the device is currently using the default password. If | auth |
| GET | `/logout` | Logs out the current session | auth |
| POST | `/network/debug/capture/start` | Start the capturing network packets | network |
| POST | `/network/debug/capture/stop` | Stop the capturing network packets | network |
| POST | `/network/dst` | Configures DST settings.  DST is a seasonal time change measure where  | network |
| GET | `/network/mac` | Get device MAC address | network |
| GET | `/network/management/server` | Get management server settings.  If Link is enabled - server will sync | network,link |
| GET | `/network/management/server/certificate` | Returns info about using certificate for Link remote server MQTT proto | network,link |
| POST | `/network/management/server/certificate` | Uploades certificate (PEM format) for Link remote server settings with | network,link |
| POST | `/network/ntp` | Set NTP server address | network |
| GET | `/network/settings` | Returns network settings. If DHCP option is enabled, response will con | network |
| POST | `/network/settings/dhcp` | Turn on DHCP. Network will be automatically configured by DHCP server. | network |
| POST | `/network/settings/static` | Set static network settings and turn off DHCP | network |
| GET | `/network/timezone` | Get current timezone and list of available timezones | network |
| POST | `/network/timezone` | Set device timezone. NTP server address must be set. | network |
| GET | `/network/wifi/access-point` | Get information about the current Wi-Fi access point settings | network,wifi |
| POST | `/network/wifi/access-point` | Set the Wi-Fi access point settings | network,wifi |
| GET | `/network/wifi/mode` | Get Wi-Fi mode | network,wifi |
| GET | `/network/wifi/settings` | Returns Wi-Fi settings. If DHCP option is enabled, response will conta | network,wifi |
| POST | `/network/wifi/settings/dhcp` | Turn on dhcp | network,wifi |
| POST | `/network/wifi/settings/static` | Set Wi-Fi static settings and turn off dhcp | network,wifi |
| GET | `/photo/file` | Takes snapshot from device camera and returns image converted to Base6 | camera |
| DELETE | `/security/banlist` | Removes all IP addresses from the ban list and unbans them - Available | security |
| GET | `/security/banlist` | Returns the list of banned IPs - Available on all panels | security |
| PUT | `/security/banlist` | Bans the single IP address or an array of addresses for the certain pe | security |
| DELETE | `/security/whitelist` | Removes all IP addresses from the white list - Available on all panels | security |
| GET | `/security/whitelist` | Returns the list of allowed IPs - Available on all panels | security |
| POST | `/security/whitelist` | Deletes the IP addresses from the white list - Available on all panels | security |
| PUT | `/security/whitelist` | Adds the IP addresses from the white list - Available on all panels | security |
| GET | `/system/analytics` | Returns whether device analytics collection is enabled. Available only | system |
| POST | `/system/analytics` | Enables or disables device analytics collection. Available only for th | system |
| POST | `/system/data/clear` | Removes table data, such as identifiers, apartments, access rules, for | system |
| POST | `/system/debug/call/end` | Stop outgoing debug call | system |
| POST | `/system/debug/call/start` | Makes an outgoing call from device - Use this endpoint for call debug. | system |
| GET | `/system/debug/call/status` | Returns debug outgoing call status info | system |
| GET | `/system/firmware/check/status` | Checks for firmware update on the server and returns info about latest | system |
| POST | `/system/firmware/server/custom` | Get custom firmware updates server settings. Can be used if the user h | system |
| POST | `/system/firmware/update/server` | - Starts upgrading firmware from server - Action can be performed if n | system |
| GET | `/system/reboot/run` | Reboot device | system |
| GET | `/system/settings/backup/all` | Get password-protected archive with device settings.  Backup does not  | system |
| GET | `/system/settings/tables` | Get password-protected archive with users data: identifiers, apartment | system |
| POST | `/system/settings/tables` | Restore users data from file | system |
| GET | `/system/support/service` | Describes feature status, support team will be allowed to connect if v | system |
| POST | `/system/support/service` | Enable/disable "remote connection" feature | system |
