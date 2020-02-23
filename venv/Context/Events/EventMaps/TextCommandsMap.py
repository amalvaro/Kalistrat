
from Context.Util.Map.Map import Map, BaseElement
from Context.Events.MessageActions.TextMessageCommands.KickCommand import KickCommand
from Context.Events.MessageActions.TextMessageCommands.SetupCommand import SetupCommand
from Context.Events.MessageActions.TextMessageCommands.HelpCommand import HelpCommand
from Context.Events.MessageActions.TextMessageCommands.MuteCommand import MuteCommand
from Context.Events.MessageActions.TextMessageCommands.UnmuteCommand import UnmuteCommand

TextCommandsMap = [

    BaseElement(SetupCommand, "setup",         {"level": 0, 'count_args': 1, 'args_exc': "Введите /setup [userId]"}),

    # Help command
    BaseElement(HelpCommand, "help",           {"level": 0, 'count_args': 1, 'args_exc': "Введите /help"}),

    # Moderator
    BaseElement(KickCommand, "kick",           {"level": 1, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(MuteCommand, "mute",           {"level": 1, 'count_args': 3, 'args_exc': "Введите /mute [userId] [reason]"}),
    BaseElement(UnmuteCommand, "unmute",       {"level": 1, 'count_args': 2, 'args_exc': "Введите /unmute [userId]"}),

    # Administrator
    BaseElement(HelpCommand, "addmoder",       {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "removemoder",    {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "moderlist",      {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "ban",            {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "unban",          {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "banlist",        {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "getban",         {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "warn",           {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "unwarn",         {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "getwarn",        {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "warnlist",       {"level": 2, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),

    # Spec administrator
    BaseElement(HelpCommand, "addadmin",       {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "removeadmin",    {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "adminlist",      {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "filter",         {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "rfilter",        {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "flist",          {"level": 3, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),

    # Creator
    BaseElement(HelpCommand, "addspec",        {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "removespec",     {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "speclist",       {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "калистрат",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "demote",         {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "kickgroup",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "kicktitle",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "kickzakrep",     {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"}),
    BaseElement(HelpCommand, "kickphoto",      {"level": 4, 'count_args': 2, 'args_exc': "Введите /kick [userId]"})
]