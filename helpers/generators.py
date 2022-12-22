import string , random
import uuid
from client.models import (
    ScoreCriteriaOption , ScoreCriteriaCategory , Offer
) 
from account.models import UserBvn

class CustomValuesGenerator:

    


    def random_bvn() -> list:
        """
        Generate random ten digit number that can be used in replace of actual BVN.
        :params :: k >> length of numbers to generate
        eg:
            random_bvn(2)  this return something like the following
            ['5232704932','0292004932']    
        """
        m = [
        {
            "first_name":"Joseph",
            "last_name":"Afolayan",
            "middle_name":"Akorede",
            "date_of_birth":"1989-08-10",
            "phone":"+2349082566578",
            "email":"afolayan35@yahoo.com",
            "gender":"male",
            "marital":"married",
            "lga":"Lagos Mainland",
            "state":"Lagos",
            "nationality":"Nigeria",
            "mixing":"0123456789",
            "reference":"adbe71ae-f6c6-425a-bb78-2c179bb6a18f"
        },
        {
            "first_name":"Chukwumeka",
            "last_name":"Praise",
            "middle_name":"Esther",
            "date_of_birth":"1975-08-10",
            "phone":"+2347083596178",
            "email":"afolayan35@yahoo.com",
            "gender":"female",
            "marital":"married",
            "lga":"Kwara East",
            "state":"Kwara",
            "nationality":"Nigeria",
            "mixing":"0859345678",
            "reference":"adbe71ae-f6c6-425a-bb78-2c177779bb6a18f"
        },
        {
            "first_name":"Demola",
            "last_name":"Ibrahim",
            "middle_name":"Sodiq",
            "date_of_birth":"2000-04-11",
            "phone":"+2348122441159",
            "email":"ibrahimdemola@gmail.com",
            "gender":"male",
            "marital":"single",
            "lga":"Shomolu",
            "state":"Lagos",
            "nationality":"Nigeria",
            "mixing":"3456789629",
            "reference":"1493a07f-77ab-4673-8844-48224d5e5bbd"
        }
    ]
        # if not isinstance(k,int) :  
        #     raise TypeError('Invalid argument type . %d is not of type int' % (k))
        result = []
        for val in m: 
            number = ''.join( str(m) for m in random.choices([0,1,2,3,4,5,6,7,8,9],k=10))
            result.append(number)
            bvn = UserBvn(
                first_name= val['first_name'],
                last_name= val['last_name'],
                middle_name = val['middle_name'],
                gender = val['gender'],
                email = val['email'],
                phone = val['phone'],
                date_of_birth = val['date_of_birth'],
                marital = val['marital'],
                lga = val['lga'],
                state = val['state'],
                nationality = val['nationality'],
                mixing = number,
            )
            # bvn.reference = uuid.uuid4().hex 
            bvn.save()


        return result



    def score_criteria()-> None:   
        """
        Generate and save the score criteria and criteria options to db.
        """
        # Personal info
        personal = ScoreCriteriaCategory.objects.create(name='Personal info')
        male = ScoreCriteriaOption.objects.create(category=personal, name='Male' , points=5)
        female = ScoreCriteriaOption.objects.create(category=personal, name='Female' , points=3)
        children_one = ScoreCriteriaOption.objects.create(category=personal, name='1 child' , points=10 )
        children_two = ScoreCriteriaOption.objects.create(category=personal, name='2 children' , points=6 )
        children_other = ScoreCriteriaOption.objects.create(category=personal, name='Above 2' , points=2 )
        married = ScoreCriteriaOption.objects.create(category=personal, name='Married' , points=10)
        single = ScoreCriteriaOption.objects.create(category=personal, name='Single' , points=5)
        divorce = ScoreCriteriaOption.objects.create(category=personal, name='Divorce' , points=7)

        # Education and employment
        edu_and_employ = ScoreCriteriaCategory.objects.create(name='Education and employment')
        undergraduate = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Undergraduate' , points=5)
        graduate = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Graduate' , points=10)
        olevel = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Olevel' , points=3)
        technical = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Technical' , points=8)
        unemployed = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Unemployed' , points=5)
        employed = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Employed' , points=10)
        entrepreneur = ScoreCriteriaOption.objects.create(category=edu_and_employ , name='Entrepreneur' , points=8)



        # years at work
        work = ScoreCriteriaCategory.objects.create(name='Work')
        less_than_six_month = ScoreCriteriaOption.objects.create(category=work , name='Less than 6 months' , points=0)
        less_than_six_month = ScoreCriteriaOption.objects.create(category=work , name='6 months' , points=1)
        one_year = ScoreCriteriaOption.objects.create(category=work , name='1 year' , points=2)
        two_year = ScoreCriteriaOption.objects.create(category=work , name='2 years' , points=3)
        above_two_year = ScoreCriteriaOption.objects.create(category=work , name='Above 2 years' , points=5 ) 

        #  type of residence
        residence = ScoreCriteriaCategory.objects.create(name='Residence')
        owned = ScoreCriteriaOption.objects.create(category=residence , name='Owned' , points=10)
        rented = ScoreCriteriaOption.objects.create(category=residence , name='Rented' , points=5)
        less_than_six_month = ScoreCriteriaOption.objects.create(category=residence , name='6 months' , points=5)
        one_year = ScoreCriteriaOption.objects.create(category=residence , name='1 year' , points=7)
        two_year = ScoreCriteriaOption.objects.create(category=residence , name='2 years' , points=8)
        above_two_year = ScoreCriteriaOption.objects.create(category=residence , name='Above 2 years' , points=10 )

        # loan reason
        loan_reason = ScoreCriteriaCategory.objects.create(name='Loan Reason')
        education = ScoreCriteriaOption.objects.create(category=loan_reason , name='Education' , points=5)
        medical = ScoreCriteriaOption.objects.create(category=loan_reason , name='Medical' , points=4)
        rent = ScoreCriteriaOption.objects.create(category=loan_reason , name='Rent' , points=5)
        travel = ScoreCriteriaOption.objects.create(category=loan_reason , name='Travel' , points=4)
        business = ScoreCriteriaOption.objects.create(category=loan_reason , name='Business' , points=10)
        goods = ScoreCriteriaOption.objects.create(category=loan_reason , name='Goods' , points=10)
        event = ScoreCriteriaOption.objects.create(category=loan_reason , name='event' , points=7)
        household = ScoreCriteriaOption.objects.create(category=loan_reason , name='Household' , points=6)
        other_reason = ScoreCriteriaOption.objects.create(category=loan_reason , name='Other' , points=2)

        # crc
        crc = ScoreCriteriaCategory.objects.create(name='CRC')
        education = ScoreCriteriaOption.objects.create(category=crc , name='Performing' , points=20)
        medical = ScoreCriteriaOption.objects.create(category=crc , name='Non performing' , points=1)
        


    def create_offers():
        Offer.objects.create(count=3, percentage=5)
        Offer.objects.create(count=6, percentage=10)
        Offer.objects.create(count=9, percentage=15)
        Offer.objects.create(count=12, percentage=20)










