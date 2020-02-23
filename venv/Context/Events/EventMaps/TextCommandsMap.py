
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.MessageActions.TextMessageCommands.KickCommand import KickCommand
from Context.Events.MessageActions.TextMessageCommands.SetupCommand import SetupCommand
from Context.Events.MessageActions.TextMessageCommands.HelpCommand import HelpCommand
from Context.Events.MessageActions.TextMessageCommands.MuteCommand import MuteCommand
from Context.Events.MessageActions.TextMessageCommands.UnmuteCommand import UnmuteCommand
from Context.Events.MessageActions.TextMessageCommands.AddmoderCommand import AddmoderCommand
from Context.Events.MessageActions.TextMessageCommands.RemovemoderCommand import RemovemoderCommand
from Context.Events.MessageActions.TextMessageCommands.ModerlistCommand import ModerlistCommand
from Context.Events.MessageActions.TextMessageCommands.BanCommand import BanCommand
from Context.Events.MessageActions.TextMessageCommands.UnbanCommand import UnbanCommand
from Context.Events.MessageActions.TextMessageCommands.BanlistCommand import BanlistCommand
from Context.Events.MessageActions.TextMessageCommands.GetbanCommand import GetbanCommand
from Context.Events.MessageActions.TextMessageCommands.WarnCommand import WarnCommand

TextCommandsMap = [

    BaseElement(SetupCommand, "/setup",         {"level": 0, 'count_args': 1, 'args_exc': "Введите /setup [userId]"}),

    # Help command
    BaseElement(HelpCommand, "/help",           {"level": 0, 'count_args': 1, 'args_exc': "Введите /help"}),

    # Moderator
    BaseElement(KickCommand, "/kick",           {"level": 1, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(MuteCommand, "/mute",           {"level": 1, 'count_args': 3, 'args_exc': "Введите /mute [userId] [reason]"}),
    BaseElement(UnmuteCommand, "/unmute",       {"level": 1, 'count_args': 2, 'args_exc': "Введите /unmute [userId]"}),

    # Administrator
    BaseElement(AddmoderCommand, "/setmoder",   {"level": 2, 'count_args': 2, 'args_exc': "Введите /setmoder [userId]"}),
    BaseElement(RemovemoderCommand, "/rm",      {"level": 2, 'count_args': 2, 'args_exc': "Введите /rm [userId]"}),
    BaseElement(ModerlistCommand, "/moderlist",      {"level": 2, 'count_args': 1, 'args_exc': "Введите /moderlist"}),
    BaseElement(BanCommand, "/ban",            {"level": 2, 'count_args': 3, 'args_exc': "Введите /ban [userId] [reason]"}),
    BaseElement(UnbanCommand, "/unban",          {"level": 2, 'count_args': 2, 'args_exc': "Введите /unban [user/group] [link]"}),
    BaseElement(BanlistCommand, "/banlist",        {"level": 2, 'count_args': 1, 'args_exc': "Введите /banlist"}),
    BaseElement(GetbanCommand, "/getban",         {"level": 2, 'count_args': 3, 'args_exc': "Введите /getban [group/user] [link]"}),
    BaseElement(WarnCommand, "/warn",           {"level": 2, 'count_args': 3, 'args_exc': "Введите /warn [userId] [reason]"}),
    BaseElement(HelpCommand, "/unwarn",         {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/getwarn",        {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/warnlist",       {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),

    # Spec administrator
    BaseElement(HelpCommand, "/addadmin",       {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/removeadmin",    {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/adminlist",      {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/filter",         {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/rfilter",        {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/flist",          {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),

    # Creator
    BaseElement(HelpCommand, "/addspec",        {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/removespec",     {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/speclist",       {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/калистрат",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/demote",         {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/kickgroup",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/kicktitle",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/kickzakrep",     {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "/kickphoto",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"})
]