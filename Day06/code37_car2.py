# 차 부모클래스
class Car :
    # Mother Class
    __name = '자동차'
    __color = 'white'
    __plate_number = ''
    __prodoct_year = 1900

    def __str__(self) :
        return f'부모클래스'

    def rub(self) :
        return f'차가 달립니다.'
    
    def stop(self) :
        return f'차가 멈춥니다.'