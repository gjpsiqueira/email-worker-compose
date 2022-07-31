create database email_sender;

\c email_sender

create table emails (
    id serial not null,
    date_recorded timestamp not null default current_timestamp,
    subject_d varchar(200) not null,
    message_d varchar(250) not null
);

