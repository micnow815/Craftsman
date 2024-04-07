SLASH_EXPORT1 = '/ce';

-- This function will create a frame and an edit box the first time it's called.
-- Subsequent calls will reuse the existing frame and edit box.
local function CreateOrShowSkillListFrame()
    if not MySkillListFrame then
        -- Create the main frame
        MySkillListFrame = CreateFrame("Frame", "MySkillListFrame", UIParent, "DialogBoxFrame")
        MySkillListFrame:SetWidth(400)
        MySkillListFrame:SetHeight(300)
        MySkillListFrame:SetPoint("CENTER", UIParent, "CENTER", 0, 0)
        MySkillListFrame:SetBackdrop({
            bgFile = "Interface\\DialogFrame\\UI-DialogBox-Background",
            edgeFile = "Interface\\DialogFrame\\UI-DialogBox-Border",
            tile = true, tileSize = 32, edgeSize = 32,
            insets = { left = 8, right = 8, top = 8, bottom = 8 }
        })
        MySkillListFrame:SetBackdropColor(0,0,0,1)
        MySkillListFrame:SetMovable(true)
        MySkillListFrame:EnableMouse(true)
        MySkillListFrame:RegisterForDrag("LeftButton")
        MySkillListFrame:SetScript("OnDragStart", MySkillListFrame.StartMoving)
        MySkillListFrame:SetScript("OnDragStop", MySkillListFrame.StopMovingOrSizing)
        MySkillListFrame:Hide()  -- Initially hidden; we'll show it after populating the EditBox
        
        -- Create the EditBox
        local editBox = CreateFrame("EditBox", nil, MySkillListFrame)
        editBox:SetMultiLine(true)
        editBox:SetWidth(370)
        editBox:SetHeight(200)
        editBox:SetPoint("TOPLEFT", MySkillListFrame, "TOPLEFT", 10, -30)
        editBox:SetFontObject("ChatFontNormal")
        editBox:SetAutoFocus(false)
        editBox:SetScript("OnEscapePressed", function() MySkillListFrame:Hide() end)
        
        -- Close button
        local closeButton = CreateFrame("Button", nil, MySkillListFrame, "UIPanelCloseButton")
        closeButton:SetPoint("TOPRIGHT", MySkillListFrame, "TOPRIGHT")
        
        -- Assign the editBox to the frame for easy access later
        MySkillListFrame.editBox = editBox
    end
    
    -- Show the frame in case it was hidden previously
    MySkillListFrame:Show()
    MySkillListFrame.editBox:SetText("")  -- Clear any previous text
end

function PrintKnownTradeSkillsToFrame()
    CreateOrShowSkillListFrame()  -- Create the frame if it doesn't exist

    -- Define the string variable to hold the skills list
    local skillListText = ""
    -- Fetch and format the list of known skills
    if TradeSkillFrame and TradeSkillFrame:IsVisible() then
        local tradeSkillName, currentLevel, maxLevel = GetTradeSkillLine()
        -- Check if we have a valid tradeskill name before proceeding
        if tradeSkillName and tradeSkillName ~= "UNKNOWN" then
            -- Start the list with the tradeskill name
            skillListText = "!" .. tradeSkillName .. "\n"
            local numSkills = GetNumTradeSkills()
            if numSkills > 0 then
                for i = 1, numSkills do
                    local skillName, skillType = GetTradeSkillInfo(i)
                    -- We assume that if skillName is nil, we've hit the end of the list
                    if not skillName then break end
                    -- Add categories and skills to the list
                    if skillType == "header" then
                        skillListText = skillListText .. "@" .. skillName .. "\n"
                    elseif skillType ~= "header" then
                        skillListText = skillListText .. "-" .. skillName .. "\n"
                    end
                end
            else
                skillListText = "No known skills found for " .. tradeSkillName
            end
        else
            skillListText = "No profession selected or profession window not opened."
        end
    else
        skillListText = "Please open a profession window first."
    end

    -- Update the frame's edit box with the skill list
    MySkillListFrame.editBox:SetText(skillListText)
    -- Set the focus to the edit box so the user can scroll/copy the contents
    -- Removed the ScrollFrame and associated scrollbar logic for simplicity
end

-- Hook up the slash command
SlashCmdList["EXPORT"] = PrintKnownTradeSkillsToFrame
