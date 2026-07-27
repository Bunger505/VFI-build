require 'imports/career_mode/helpers'

----------------------------------------------------------
-- Project Victor v0.3
-- First Squad Snapshot
----------------------------------------------------------

if not IsInCM() then
    MessageBox("Project Victor", "Please load a Career Mode save first.")
    return
end

local userTeam = GetUserTeamID()

local playersTable = LE.db:GetTable("players")
local contractsTable = LE.db:GetTable("career_playercontract")

if not playersTable or not contractsTable then
    MessageBox("Project Victor", "Unable to access database tables.")
    return
end

----------------------------------------------------------
-- Build player lookup
----------------------------------------------------------

local playerLookup = {}

local record = playersTable:GetFirstRecord()

while record > 0 do

    local id = playersTable:GetRecordFieldValue(record,"playerid")

    if id then
        playerLookup[id] = record
    end

    record = playersTable:GetNextValidRecord()

end

----------------------------------------------------------
-- Build squad
----------------------------------------------------------

local squad = {}

record = contractsTable:GetFirstRecord()

while record > 0 do

    local teamid = contractsTable:GetRecordFieldValue(record,"teamid")

    if teamid == userTeam then

        local playerid = contractsTable:GetRecordFieldValue(record,"playerid")

        local playerRecord = playerLookup[playerid]

        if playerRecord then

            local player = {

                id = playerid,

                name = GetPlayerName(playerid),

                overall = playersTable:GetRecordFieldValue(playerRecord,"overallrating"),

                potential = playersTable:GetRecordFieldValue(playerRecord,"potential"),

                position = playersTable:GetRecordFieldValue(playerRecord,"preferredposition1"),

                birthdate = playersTable:GetRecordFieldValue(playerRecord,"birthdate")

            }

            table.insert(squad, player)

        end

    end

    record = contractsTable:GetNextValidRecord()

end

----------------------------------------------------------
-- Export JSON
----------------------------------------------------------

local profile = os.getenv("USERPROFILE") or "."

local filename = profile .. "\\Desktop\\club_snapshot.json"

local file = io.open(filename,"w")

if not file then

    MessageBox("Project Victor","Unable to create JSON file.")

    return

end

file:write("{\n")

file:write('  "version":"0.3",\n')

file:write('  "players":[\n')

for i,player in ipairs(squad) do

    file:write(string.format(

'    {"id":%d,"name":"%s","overall":%d,"potential":%d,"position":%d,"birthdate":%d}',

        player.id,

        player.name,

        player.overall,

        player.potential,

        player.position,

        player.birthdate

    ))

    if i < #squad then

        file:write(",")

    end

    file:write("\n")

end

file:write("  ]\n")

file:write("}")

file:close()

MessageBox(
    "Project Victor",
    "Snapshot exported!\n\n"..filename
)