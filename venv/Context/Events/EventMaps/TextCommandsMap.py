
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
from Context.Events.MessageActions.TextMessageCommands.UnwarnCommand import UnwarnCommand
from Context.Events.MessageActions.TextMessageCommands.GetwarnCommand import GetwarnCommand
from Context.Events.MessageActions.TextMessageCommands.WarnlistCommand import WarnlistCommand
from Context.Events.MessageActions.TextMessageCommands.AddadminCommand import AddadminCommand
from Context.Events.MessageActions.TextMessageCommands.AdminlistCommand import AdminlistCommand
from Context.Events.MessageActions.TextMessageCommands.FilterCommand import FilterCommand
from Context.Events.MessageActions.TextMessageCommands.RfilterCommand import RfilterCommand
from Context.Events.MessageActions.TextMessageCommands.FlistCommand import FlistCommand
from Context.Events.MessageActions.TextMessageCommands.AddspecCommand import AddspecCommand

from Context.Events.MessageActions.TextMessageCommands.SpeclistCommand import SpeclistCommand
from Context.Events.MessageActions.TextMessageCommands.KalistratCommand import KalistratCommand
from Context.Events.MessageActions.TextMessageCommands.DemoteCommand import DemoteCommand

TextCommandsMap = [

    BaseElement(SetupCommand, "/setup",         {"level": 0, 'count_args': 1, 'args_exc': "Введите /setup [userId]"}),

    # Help command
    BaseElement(HelpCommand, "/help",           {"level": 0, 'count_args': 1, 'args_exc': "Введите /help"}),

    # Moderator
    BaseElement(KickCommand, "/kick",           {"level": 1, 'count_args': 2, 'args_exc': "Введите /kick [mention]"}),
    BaseElement(MuteCommand, "/mute",           {"level": 1, 'count_args': 3, 'args_exc': "Введите /mute [mention] [reason]"}),
    BaseElement(UnmuteCommand, "/unmute",       {"level": 1, 'count_args': 2, 'args_exc': "Введите /unmute [mention]"}),

    # Administrator
    BaseElement(AddmoderCommand, "/setmoder",   {"level": 2, 'count_args': 2, 'args_exc': "Введите /setmoder [mention]"}),
    BaseElement(RemovemoderCommand, "/rm",      {"level": 2, 'count_args': 2, 'args_exc': "Введите /rm [mention]"}),
    BaseElement(ModerlistCommand, "/moderlist",      {"level": 2, 'count_args': 1, 'args_exc': "Введите /moderlist"}),
    BaseElement(BanCommand, "/ban",            {"level": 2, 'count_args': 3, 'args_exc': "Введите /ban [mention] [reason]"}),
    BaseElement(UnbanCommand, "/unban",          {"level": 2, 'count_args': 2, 'args_exc': "Введите /unban [user/group] [link]"}),
    BaseElement(BanlistCommand, "/banlist",        {"level": 2, 'count_args': 1, 'args_exc': "Введите /banlist"}),
    BaseElement(GetbanCommand, "/getban",         {"level": 2, 'count_args': 3, 'args_exc': "Введите /getban [group/user] [link]"}),
    BaseElement(WarnCommand, "/warn",           {"level": 2, 'count_args': 3, 'args_exc': "Введите /warn [mention] [reason]"}),
    BaseElement(UnwarnCommand, "/unwarn",         {"level": 2, 'count_args': 2, 'args_exc': "Введите /unwarn [[group/user], если указана ссылка] [link/mention]"}),
    BaseElement(GetwarnCommand, "/getwarn",        {"level": 2, 'count_args': 2, 'args_exc': "Введите /getwarn [mention]"}),
    BaseElement(WarnlistCommand, "/warnlist",       {"level": 2, 'count_args': 1, 'args_exc': "Введите /warnlist"}),

    # Spec administrator
    BaseElement(AddadminCommand, "/setadmin",       {"level": 3, 'count_args': 2, 'args_exc': "Введите /setadmin [mention]"}),
    BaseElement(AdminlistCommand, "/adminlist",      {"level": 3, 'count_args': 1, 'args_exc': "Введите /adminlist"}),
    BaseElement(FilterCommand, "/filter",         {"level": 3, 'count_args': 2, 'args_exc': "Введите /filter [word(s) ..]"}),
    BaseElement(RfilterCommand, "/rfilter",        {"level": 3, 'count_args': 2, 'args_exc': "Введите /rfilter [word(s) ..]"}),
    BaseElement(FlistCommand, "/flist",          {"level": 3, 'count_args': 1, 'args_exc': "Введите /flist"}),

    # Creator
    BaseElement(AddspecCommand, "/setgaadm",        {"level": 4, 'count_args': 2, 'args_exc': "Введите /setgaadm [mention]"}),
    BaseElement(SpeclistCommand, "/gaadmlist",       {"level": 4, 'count_args': 1, 'args_exc': "Введите /gaadmlist"}),
    BaseElement(KalistratCommand, "/калистрат",      {"level": 4, 'count_args': 1, 'args_exc': "Введите /калистрат"}),
    BaseElement(DemoteCommand, "/demote",         {"level": 4, 'count_args': 1, 'args_exc': "Введите /demote"}),
    BaseElement(HelpCommand, "/kickgroup",      {"level": 4, 'count_args': 1, 'args_exc': "Введите /kickgroup"}),
    BaseElement(HelpCommand, "/kicktitle",      {"level": 4, 'count_args': 1, 'args_exc': "Введите /kicktitle"}),
    BaseElement(HelpCommand, "/kickzakrep",     {"level": 4, 'count_args': 1, 'args_exc': "Введите /kickzakrep"}),
    BaseElement(HelpCommand, "/kickphoto",      {"level": 4, 'count_args': 1, 'args_exc': "Введите /kickphoto"})
]