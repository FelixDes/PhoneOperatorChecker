drop table if exists PhoneNumbers;
drop table if exists MovedPhoneNumbers;

CREATE TABLE PhoneNumbers
(
    code         INT,
    rangeStart   bigint,
    rangeEnd     bigint,
    amount       bigint,
    operatorName VARCHAR(512),
    location     VARCHAR(512)
);

COPY PhoneNumbers (code, rangeStart, rangeEnd, amount, operatorName, location)
    FROM '/Numbers-Plan-9.csv'
    DELIMITER ';'
    CSV HEADER;


CREATE TABLE MovedPhoneNumbers
(
    phoneNumber  bigint,
    operatorName VARCHAR(512)
);

COPY MovedPhoneNumbers (phoneNumber, operatorName)
    FROM '/MNP.csv'
    DELIMITER ','
    CSV HEADER;

create function get_number_operator(pn bigint)
    returns VARCHAR(512)
    language plpgsql
as
$$
begin
    return (select COALESCE((select operatorName from MovedPhoneNumbers where phonenumber = pn),
                    (select operatorName from PhoneNumbers ps where pn / 10000000 = ps.code and
                    mod(pn, 10000000)between ps.rangestart and ps.rangeend)));
end;
$$;