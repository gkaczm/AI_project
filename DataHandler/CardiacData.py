class CardiacData:

    def __init__(self, qrs_dur, pr_int, qt_int, t_int, p_int, qrs, t, p, qrst, j):
        self.qrs_duration = qrs_dur
        self.pr_interval = pr_int
        self.qt_interval = qt_int
        self.t_int = t_int
        self.p_interval = p_int

        self.qrs_vector_angle = qrs
        self.t_vector_angle = t
        self.p_vector_angle = p
        self.qrst_vector_angle = qrst
        self.j_vector_angle = j
