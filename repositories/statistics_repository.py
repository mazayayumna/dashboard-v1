from app.models.disease_statistic import DiseaseStatistic

class StatisticRepository:

    def save(
        self,
        db,
        statistic
    ):
        db.add(statistic)
        db.commit()
        db.refresh(statistic)
        return statistic